import heapq


class Solution:
  """
    @param: k: An integer
    """

  def __init__(self, k):
    # do intialization if necessary
    self.hp = []
    self.k = k

  """
    @param: num: Number to be added
    @return: nothing
    """

  def add(self, num):
    # write your code here
    heapq.heappush(self.hp, -num)

  """
    @return: Top k element
    """

  def topk(self):
    # write your code here
    hp2 = self.hp[:]
    tk = []
    for ik in range(min(len(hp2), self.k)):
      tk.append(-heapq.heappop(hp2))
    return tk
