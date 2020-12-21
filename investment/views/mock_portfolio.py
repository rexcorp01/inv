"""
mock_portfolio
~~~~~~~~~~~~~~~
模拟组合来对比调仓对业绩的影响
@date: 2020-12-16
"""

import pandas as pd
import numpy as np
from copy import deepcopy
from django.http import JsonResponse
from investment import models
from investment.views.backtest import BackTestView


def change_date(request):
    """获取全部调仓日期

    Args:
        request: django request object

    Returns:
        List[datetime.date]: 调仓日期
    """
    port_code: str = request.GET.get('portCode')
    dates = models.Transactions.objects.filter(
        port_code=port_code, operation__contains='成交确认'
    ).distinct().values('date')
    dates = sorted([x['date'].strftime('%Y-%m-%d') for x in dates], reverse=True)
    return JsonResponse({'data': dates})


def change_detail(request):
    """调仓记录

    Args:
        request: django request object

    Returns:
        详细调仓记录

    """
    port_code: str = request.GET.get('portCode')
    date: str = request.GET.get('date')
    trans = models.Transactions.objects.filter(
        port_code=port_code, date=date, operation__contains='成交确认'
    ).all()
    ret = []
    for x in trans:
        op = x.operation
        if '赎回' in op:
            r = {'secucode': x.secucode, 'operation': '赎回', 'amount': x.order_value, 'measure': '份'}
        elif '申购' in op:
            r = {'secucode': x.secucode, 'operation': '申购', 'amount': x.order_value, 'measure': '元'}
        elif '转出' in op:
            r = {'secucode': x.secucode, 'operation': '转出', 'amount': x.order_value, 'measure': '份'}
        else:
            r = {'secucode': x.secucode, 'operation': '转入', 'amount': x.order_value, 'measure': '元'}
        ret.append(r)
    return JsonResponse({'data': ret})


def mock(request):
    """模拟业绩

    选择一个实际已经调仓的成交确认日期，计算不调仓和调仓后的走势
    根据当前持仓和交易流水，还原调仓前持仓
    Args:
        request: django request

    Returns:
        业绩对比
    """
    port_code: str = request.GET.get('portCode')
    date: str = request.GET.get('date')
    # 调仓后持仓
    holding = models.Holding.objects.filter(
        port_code=port_code, date=date
    ).values('secucode', 'holding_value', 'mkt_cap')
    holding = {x['secucode']: float(x['holding_value']) for x in holding}
    holding.update({'cny': 0})
    trans = models.Transactions.objects.filter(
        port_code=port_code, date=date, operation__contains='成交确认'
    ).all()
    mock_holding = deepcopy(holding)
    for x in trans:
        op = x.operation
        if '赎回' in op:
            mock_holding[x.secucode] += float(x.order_value)
            mock_holding['cny'] -= float(x.operation_amount)
        elif '申购' in op:
            mock_holding[x.secucode] -= float(x.order_value)
            mock_holding['cny'] += -float(x.operation_amount)

        # 转入和转出是相对应的，有转出就有转入，转换操作会影响费用
        elif '转出' in op:
            mock_holding[x.secucode] += float(x.order_value)
            mock_holding['cny'] += float(x.fee)
        else:
            mock_holding[x.secucode] -= float(x.order_value)
            mock_holding['cny'] += float(x.fee)
    funds = list(holding.keys())
    weight = np.array([list(holding.values()), list(mock_holding.values())])
    nav = models.FundAdjPrice.objects.filter(secucode__in=funds, date__gte=date).values('secucode', 'date', 'adj_nav')
    nav = pd.DataFrame(nav)
    nav.adj_nav = nav.adj_nav.astype('float')
    nav = nav.pivot_table(index='date', columns='secucode', values=['adj_nav'])['adj_nav']
    nav = nav.dropna(how='any')
    nav['cny'] = 1
    nav = nav.loc[:, funds]
    ret = np.dot(weight, nav.values.T)
    index = [x.strftime('%Y-%m-%d') for x in nav.index]
    ret = pd.DataFrame(ret.T, columns=['调仓组合', '不调仓组合'], index=index)
    ret = ret / ret.iloc[0, :]
    perf = BackTestView.calc_performance(ret)
    perf = perf.reset_index()
    perf = perf.to_dict(orient='records')
    ret = np.round(ret, 4)
    ret['date'] = ret.index
    ret = ret.to_dict(orient='records')
    return JsonResponse({'data': ret, 'perf': perf})
