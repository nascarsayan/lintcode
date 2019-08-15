class Solution:
  """
    @param temperatures: a list of daily temperatures
    @return: a list of how many days you would have to wait until a warmer temperature
    """

  def dailyTemperatures(self, temp):
    # Write your code here
    stac = []
    nex = []
    size = len(temp)
    for i in range(size - 1, -1, -1):
      while (len(stac) > 0 and temp[stac[0]] <= temp[i]):
        stac.pop(0)
      if len(stac) == 0:
        nex.insert(0, 0)
      else:
        nex.insert(0, stac[0] - i)
      stac.insert(0, i)
    return nex
