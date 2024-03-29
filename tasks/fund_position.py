import datetime
from itertools import groupby
from typing import Dict, List, Union

import arrow
import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn import preprocessing

from tasks import models
from rpc.fund_screen_client import Client


# 基金仓位约束
BOUNDS = {
    '标准股票型': (0.8, 1),
    '混合偏股型': (0.5, 0.95),
    '股债平衡型': (0.2, 0.8),
    '灵活配置型': (0.05, 0.95)
}

MAPPER = {
    '标准股票型': 'normal_stock',
    '混合偏股型': 'mix_stock',
    '股债平衡型': 'mix_equal',
    '灵活配置型': 'mix_flexible'
}

LAUNCH = Client.simple('fund_basic')


def fund_style() -> Dict[str, List[str]]:
    """基金类型

    Returns:
        {
            '标准股票型基金': [],
            '偏股混合型基金': [],
            '平衡混合型基金': [],
            '灵活配置型基金': []
        }
    """
    funds = Client.simple('fund_category', [])
    funds = [x for x in funds if x['second'] in MAPPER.keys()]
    funds = sorted(funds, key=lambda x: x['second'])
    funds = groupby(funds, key=lambda x: x['second'])
    funds = {x[0]: [y['secucode'] for y in x[1]] for x in funds}
    return funds


def date_before_target(day: datetime.date, days: int = 40) -> datetime.date:
    """指定日期的n个交易日前的日期

    Args:
        day: 指定日期
        days: 时间差，按照经验，40日回归结果比较平稳

    Returns:
        datetime.date
    """
    start: datetime.date = day - datetime.timedelta(days=days*2)
    td = models.TradingDays.objects.filter(date__range=(start, day)).order_by('date')
    td = [x.date for x in td]
    start = td[-days]
    return start


def tradingday_between_dates(start, end):
    dates = models.TradingDays.objects.filter(date__gt=start, date__lte=end).all()
    dates = [x.date for x in dates]
    return dates


def benchmark_close_price(secucode: str, date: datetime.date) -> pd.DataFrame:
    """基准指数收盘价

    Args:
        secucode: 基准代码
        date: 截止日

    Returns:

    """
    start = date_before_target(date)
    cp = models.IndexQuote.objects.filter(secucode=secucode, date__range=(start, date)).values('date', 'close')
    cp = pd.DataFrame(cp).set_index('date').rename(columns={'close': secucode}).astype('float')
    return cp


def fund_nav(funds: List[str], date: datetime.date) -> pd.DataFrame:
    """获取基金净值

    Args:
        funds: 基金列表
        date: 截止日

    Returns:

    """
    start = date_before_target(date)
    before = (start - datetime.timedelta(days=90))
    funds = [x for x in funds if arrow.get(LAUNCH.get(x, datetime.date.today())).date() <= before]
    nav = models.FundPrice.objects.filter(
        secucode__in=funds, date__range=(start, date)
    ).values('secucode', 'date', 'nav')
    nav = pd.DataFrame(nav)
    nav.nav = nav.nav.astype('float')
    nav = nav.pivot_table(index='date', columns='secucode', values='nav')
    return nav


def estimate(x: np.matrix, y: np.matrix):
    """估算单只基金仓位

    在估算前需要标准化数据
    Args:
        x: 基准日度涨跌幅
        y: 基金净值日度涨跌幅

    Returns:

    """
    x = preprocessing.scale(x)
    y = preprocessing.scale(y)
    model = Lasso(alpha=0.001, max_iter=10000, positive=True)
    model.fit(x, y)
    coefficient = model.coef_
    return coefficient


def calc(date: datetime.date) -> Dict[str, Union[float, datetime.date]]:
    """计算各类基金估算仓位

    Returns:

    """
    funds = fund_style()
    benchmark = '000905'
    ret = {'date': date}
    for name, fund in funds.items():
        nav = fund_nav(fund, date)
        ben = benchmark_close_price(benchmark, date)
        nav = ben.merge(nav, left_index=True, right_index=True, how='inner')
        nav = nav.dropna(how='any', axis=1)
        nav = nav.pct_change().dropna()
        y = np.asmatrix(nav.iloc[:, 1:])
        x = np.asmatrix(nav[benchmark]).T
        c = estimate(x, y)
        min_, max_ = BOUNDS[name]
        c = c.reshape(1, -1)[0]
        c = [x for x in c if all([x >= min_, x <= max_])]
        ret[MAPPER[name]] = sum(c)/len(c)
    return ret


def commit() -> None:
    date: datetime.date = models.FundPrice.objects.latest('date').date
    exist = models.FundPosEstimate.objects.latest()
    if not exist:
        start = date_before_target(date, 90)
    else:
        start = exist.date
    if date == start:
        return
    dates = tradingday_between_dates(start, date)
    fps = []
    for d in dates:
        ret = calc(d)
        m = models.FundPosEstimate(**ret)
        fps.append(m)
    models.FundPosEstimate.objects.bulk_create(fps)


def commit_bulk():
    """初始化时使用"""
    date: datetime.date = models.FundPrice.objects.latest('date').date
    start = datetime.date(2020, 1, 1)
    dates = tradingday_between_dates(start, date)
    fps = []
    for d in dates:
        print(d)
        ret = calc(d)
        fps.append(ret)
    fps = pd.DataFrame(fps)
    fps.to_excel('c:/users/chuanchao.peng/desktop/基金仓位估算.xlsx', index=False)


if __name__ == '__main__':
    commit()
