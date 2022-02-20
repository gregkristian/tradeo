# Class to trade one investment. Currently support only buy all or sell all

class Trader:
  def __init__(self, init_amount):
    self.init_amount = init_amount
    self.curr_amount = init_amount
    self.shares = 0
    self.state = 0 # currently not invested

  def buy(self, buy_price):
    if self.curr_amount < 1:
      return False
    self.shares = self.curr_amount / buy_price
    self.curr_amount = 0
    self.state = 1
    return True

  def sell(self, sell_price):
    if self.shares == 0:
      return False
    self.curr_amount = self.shares * sell_price
    self.shares = 0
    self.state = 0
    return True

  def get_profit(self):
    return self.curr_amount - self.init_amount