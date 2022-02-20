# Backtester for trading strategy
import pytest
from trader import Trader

def test_trader_class():
    init_capital = 1000
    buy_price = 50
    sell_price = 70

    stock_x = Trader(init_capital)
    stock_x.buy(buy_price)
    stock_x.sell(sell_price)

    exp_profit = (init_capital / buy_price * sell_price) - init_capital

    assert stock_x.get_profit() == exp_profit
