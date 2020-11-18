"""
command
~~~~~~~~~~~~~~~~~~~~~~~
@author: chuanchao.peng
@date: 2020-09-07
@desc:
"""
import click

from sql import tools
from shu.to_database import run as shu_run


@click.group()
def root():
    pass


@root.group()
def index():
    pass


@root.command()
def fund():
    tools.commit_fund()


@root.command()
def stock():
    tools.commit_stocks()


@root.command()
def tradingday():
    tools.commit_trading_day()


@index.command()
def gil():
    tools.commit_index_gil()


@index.command()
def wind():
    tools.commit_index_wind()


@index.command()
def run_index():
    tools.commit_index()


@root.command()
def shu():
    shu_run()


# 'commit_index', 'commit_index_gil', 'commit_index_wind', 'commit_fund', 'commit_trading_day', 'commit_stocks'
@click.command()
def run_all():
    shu_run()
    tools.commit_stocks()
    tools.commit_fund()
    tools.commit_index()
    tools.commit_tradingdays()


if __name__ == '__main__':
    root()
