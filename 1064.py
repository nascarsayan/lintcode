class MyCalendarTwo:

  def __init__(self):
    self.sects = []
    self.intvs = []

  def book(self, start, end):
    """
    :type start: int
    :type end: int
    :rtype: bool
    """
    for sect in self.sects:
      if max(sect[0], start) < min(sect[1], end):
        return False
    newsect = []
    for intv in self.intvs:
      inst = max(intv[0], start)
      infl = min(intv[1], end)
      if inst < infl:
        newsect.append([inst, infl])
    self.sects.extend(newsect)
    self.intvs.append([start, end])
    return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
