class Solution:
  """
    @param heights: a list of integers
    @return: a integer
    """

  def trapRainWater(self, heights):
    # write your code here
    size = len(heights)
    if size < 3:
      return 0
    lmax = [None] * size
    rmax = lmax[:]
    lmax[0] = heights[0]
    rmax[-1] = heights[-1]
    trap = 0
    for idx in range(1, size):
      lmax[idx] = max(lmax[idx - 1], heights[idx])

    for idx in range(size - 2, -1, -1):
      rmax[idx] = max(rmax[idx + 1], heights[idx])

    for idx in range(1, size - 1):
      trap += min(lmax[idx], rmax[idx]) - heights[idx]
    return trap


# print(Solution().trapRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
