"""
单只基金相关的功能
"""

from investment.models import Funds, FundStyle


def fund_names(funds):
    """获取基金名称"""
    query_ret = Funds.objects.filter(secucode__in=funds).all()
    ret = {x.secucode: x.secuname for x in query_ret}
    return ret


def fund_is_monetary(fund: str) -> bool:
    """判断基金是否是货币基金

    Args:
        fund: 基金代码

    Returns:
        bool: 是否是货币基金
    """
    fund_type = FundStyle.objects.filter(secucode=fund).last().fundtype
    return fund_type == '货币市场型基金'
