"""
funds_extend
~~~~~~~~~~~~
扩充基金数据同步，处理复杂的同步程序
"""
import datetime
import math

from django.db.models import Max
from sql import models
from sql.sql_templates import funds
from sql.utils import read_oracle, render


def commit_holding_stock_detail():
    """同步基金完整持仓"""
    publish = '年报'
    _commit_holding_stocks(publish, funds.fund_holding_stock_detail)


def commit_holding_top_ten():
    """同步基金季报重仓股"""
    publish = '季报'
    _commit_holding_stocks(publish, funds.fund_top_ten_stock)


def commit_announcement():
    """同步基金公告数据"""
    exist = models.FundAnnouncement.objects.last()
    if exist:
        date = exist.date
    else:
        date = datetime.date.today() + datetime.timedelta(days=-30)
    date = date.strftime('%Y-%m-%d')
    sql = render(funds.fund_announcement, '<date>', date)
    data = read_oracle(sql)
    fund = models.Holding.objects.values('secucode').distinct()
    fund = [x['secucode'] for x in fund]
    fund = models.Funds.objects.filter(secucode__in=fund).all()
    fund = {x.secucode: x for x in fund}
    data.secucode = data.secucode.apply(lambda x: fund.get(x))
    data = data[data.secucode.notnull()]
    ret = (models.FundAnnouncement(**x) for _, x in data.iterrows())
    for i in ret:
        try:
            i.save()
        except Exception as e:
            print(e.__class__)


def commit_fund_advisor():
    """同步基金管理人名称数据

    Returns:

    """
    data = read_oracle(funds.fund_advisor)
    fund = models.Funds.objects.all()
    fund = {x.secucode: x for x in fund}
    exists = models.FundAdvisor.objects.all()
    exists = [x.secucode for x in exists]
    data = data[~data.secucode.isin(exists)]
    data.secucode = data.secucode.apply(lambda x: fund.get(x))
    data = data[data.secucode.notnull()]
    model = [models.FundAdvisor(**x) for _, x in data.iterrows()]
    models.FundAdvisor.objects.bulk_create(model)


def _commit_holding_stocks(publish: str, sql):
    """同步基金持仓数据

    基金持仓来源于两张表，一为重仓股，源于季报，一为完成持仓，源于半年报或年报
    """
    if models.FundHoldingStock.objects.exists():
        date = datetime.date.today()
        date = datetime.date(date.year - 1, 1, 1)
    else:
        date = datetime.date(1990, 1, 1)
    exist = models.FundHoldingStock.objects.filter(publish=publish).values('secucode').annotate(max_date=Max('date'))
    existed = {x['secucode']: x['max_date'] for x in exist}

    full = models.Funds.objects.all()
    instance = {x.secucode: x for x in full}
    sql = render(sql, '<date>', date.strftime('%Y-%m-%d'))
    data = read_oracle(sql)
    data = data[data.publish == publish]
    data.secucode = data.secucode.apply(lambda x: instance.get(x))
    data = data[data.secucode.notnull()]
    data = data[data.agg(lambda x: x.date > existed.get(x.secucode, datetime.date(1990, 1, 1)), axis=1)]
    data = data.to_dict(orient='records')
    data = [models.FundHoldingStock(**x) for x in data]
    split = math.ceil(len(data) / 10000)
    for i in range(split):
        models.FundHoldingStock.objects.bulk_create(data[i*10000: (i+1)*10000])


def commit_asset_allocate_hk():
    """sync qdii fund asset allocate

    Returns:

    """
    data = read_oracle(funds.fund_allocate_hk)
    date = dict(zip(data['secucode'], data['enddate']))
    data['assettype'] = data['assettype'].astype('str')
    ratio = data.pivot_table(index='secucode', columns='assettype', values='ratioinnv', aggfunc=sum)
    ratio = ratio.fillna(0)
    for col in ['10', '30', '10015', '40', '10075', '10089', '10090']:
        if col not in ratio.columns:
            ratio[col] = 0
    ratio['stock'] = ratio['10'] / 100
    ratio['bond'] = ratio['30']
    ratio['metals'] = ratio['40'] / 100
    ratio['fund'] = ratio['10015'] / 100
    ratio['monetary'] = (ratio['10075'] + ratio['10089']) / 100
    ratio['other'] = ratio['10090'] / 100
    ratio = ratio[['stock', 'bond', 'fund', 'metals', 'monetary', 'other']]
    ratio = ratio.reset_index()
    ratio['date'] = ratio.secucode.apply(lambda x: date.get(x))
    fund = models.Funds.objects.filter(secucode__in=list(ratio.secucode)).all()
    fund = {x.secucode: x for x in fund}
    ratio['secucode'] = ratio['secucode'].apply(lambda x: fund.get(x))
    ratio = ratio.to_dict(orient='records')
    for x in ratio:
        models.FundAssetAllocate.objects.update_or_create(secucode=x['secucode'], date=x['date'], defaults=x)


def commit_fund_holding_stock_hk():
    """基金持仓股票-港股"""
    data = read_oracle(funds.fund_holding_stock_hk)
    data['ratio'] = data['ratio'] / 100
    stocks = list(set(list(data.stockcode)))
    stocks = models.Stock.objects.filter(secucode__in=stocks).all()
    stocks = {x.secucode: x for x in stocks}
    data['stockname'] = data.stockcode.apply(lambda x: stocks.get(x).secuname if stocks.get(x) else None)
    data['stockcode'] = data.stockcode.apply(lambda x: stocks.get(x) if stocks.get(x) else None)
    data = data[data['stockcode'].notnull()]
    fund = list(set(list(data.secucode)))
    fund = models.Funds.objects.filter(secucode__in=fund).all()
    fund = {x.secucode: x for x in fund}
    data['secucode'] = data.secucode.apply(lambda x: fund.get(x))
    data = data.to_dict(orient='records')
    for x in data:
        models.FundHoldingStock.objects.update_or_create(
            secucode=x.pop('secucode'), date=x.pop('date'), stockcode=x.pop('stockcode'), defaults=x
        )


def commit_fund_quote():
    """
    同步场内基金行情数据
    Returns:
    """
    if not models.FundQuote.objects.exists():
        data = read_oracle(funds.fund_quote_once)
    else:
        data = read_oracle(funds.fund_quote)
        last = models.FundQuote.objects.values('secucode').annotate(mdate=Max('date'))
        last = {x['secucode']: x['mdate'] for x in last}
        data = data[data.agg(lambda x: x.date > last.get(x.secucode, datetime.date(2021, 1, 1)), axis=1)]
    instance = models.Funds.objects.all()
    instance = {x.secucode: x for x in instance}
    data.secucode = data.secucode.apply(lambda x: instance.get(x))
    data = data[data.secucode.notnull()]
    data = data.dropna(how='any')
    m = [models.FundQuote(**x) for _, x in data.iterrows()]
    models.FundQuote.objects.bulk_create(m)


if __name__ == '__main__':
    # commit_holding_stock_detail()
    # commit_fund_holding_stock_hk()
    commit_holding_top_ten()
    # commit_asset_allocate_hk()
    # commit_fund_quote()
