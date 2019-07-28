class Solution:
  """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """

  def canCompleteCircuit(self, gas, cost):
    # write your code here
    size = len(gas)
    net = [gas[i] - cost[i] for i in range(size)]
    if size == 0:
      return -1
    if size == 1:
      if net[0] >= 0:
        return 0
      return -1
    ltr = net[:]
    for i in range(1, size):
      ltr[i] += ltr[i - 1]
    ltrmin = ltr[:]
    for i in range(1, size):
      ltrmin[i] = min(ltrmin[i - 1], ltrmin[i])
    if ltrmin[-1] >= 0:
      return 0
    for i in range(1, size):
      if (ltrmin[-1] - ltr[i - 1] >= 0 and
          ltr[-1] - ltr[i - 1] + ltrmin[i - 1] >= 0):
        return i
    return -1


# print(Solution().canCompleteCircuit([1, 2, 3, 3], [2, 1, 5, 1]))
