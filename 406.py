class Solution:
  """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

  def minimumSize(self, nums, s):
    # write your code here
    size = len(nums)
    if size == 0:
      return -1
    total = 0
    st = 0
    inf = float('inf')
    minl = inf
    for fl in range(size):
      total += nums[fl]
      if total == s:
        minl = min(minl, fl - st + 1)
      lshift = False
      while (total > s and st < fl):
        lshift = True
        total -= nums[st]
        st += 1
      if (total == s):
        minl = min(minl, fl - st + 1)
      elif lshift:
        minl = min(minl, fl - st + 2)
      if (total > s):
        return 1
    if minl == inf:
      return -1
    return minl


# print(Solution().minimumSize([100, 50, 99, 50, 100, 50, 99, 50, 100, 50], 250))
