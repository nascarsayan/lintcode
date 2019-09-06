class StockSpanner:

  def __init__(self):
    self.stac = []
    self.arr = []
    self.cnt = 0

  """
    @param price:
    @return: int
    """

  def next(self, price):
    # Write your code here.
    while (self.stac and self.arr[self.stac[-1]] <= price):
      self.stac.pop()
    span = self.cnt + 1
    if self.stac:
      span -= self.stac[-1] + 1
    self.arr.append(price)
    self.stac.append(self.cnt)
    self.cnt += 1
    return span
