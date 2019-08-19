class ZigzagIterator2:
  """
    @param: vecs: a list of 1d vectors
    """

  def __init__(self, vecs):
    # do intialization if necessary
    self.v = []
    self.ptr = []
    for vec in vecs:
      if len(vec) > 0:
        self.ptr.append(len(self.v))
        self.v.append(vec)
    self.idx = (0, None)[len(self.v) == 0]

  """
    @return: An integer
    """

  def next(self):
    # write your code here
    if self.idx is None:
      return None
    currv = self.v[self.ptr[self.idx]]
    val = currv.pop(0)
    if len(currv) == 0:
      self.ptr.pop(self.idx)
      if len(self.ptr) > 0:
        self.idx = self.idx % len(self.ptr)
      else:
        self.idx = None
    else:
      self.idx = (self.idx + 1) % len(self.ptr)
    return val

  """
    @return: True if has next
    """

  def hasNext(self):
    # write your code here
    return self.idx is not None


# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result
