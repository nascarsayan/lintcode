class ZigzagIterator:
  """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

  def __init__(self, v1, v2):
    # do intialization if necessary
    self.v = [v1, v2]
    self.ptr = []
    if len(v1) > 0:
      self.ptr += [0]
    if len(v2) > 0:
      self.ptr += [1]
    self.idx = (0, None)[len(self.ptr) == 0]

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
      self.idx = (self.idx + 1) % len(self.ptr)
    else:
      self.idx = None
    return val

  """
    @return: True if has next
    """

  def hasNext(self):
    # write your code here
    return self.idx is not None


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result
