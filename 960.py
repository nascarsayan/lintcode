class DataStream:

  def __init__(self):
    # do intialization if necessary
    self.appear = {}
    self.isUniq = []
    self.nums = []
    self.idx = None

  """
    @param num: next number in stream
    @return: nothing
    """

  def add(self, num):
    # write your code here
    seqlen = len(self.isUniq)
    self.nums.append(num)
    if num not in self.appear:
      self.appear[num] = seqlen
      self.isUniq.append(True)
      if self.idx is None:
        self.idx = seqlen
    else:
      self.isUniq.append(False)
      fstenc = self.appear[num]
      if self.isUniq[fstenc]:
        self.isUniq[self.appear[num]] = False
        if self.idx == fstenc:
          while (self.idx < seqlen):
            if self.isUniq[self.idx]:
              return
            self.idx += 1
          self.idx = None

  """
    @return: the first unique number in stream
    """

  def firstUnique(self):
    # write your code here
    return self.nums[self.idx]
