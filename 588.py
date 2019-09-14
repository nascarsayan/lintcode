class Solution:
  """
  @param nums: a non-empty array only positive integers
  @return: true if can partition or false
  """

  def canPartition(self, nums):
    # write your code here
    tot = sum(nums)
    if tot % 2 == 1:
      return False
    subs = {0}
    for num in nums:
      nx = set()
      for sub in subs:
        nw = sub + num
        if nw <= tot // 2:
          nx.add(nw)
        if nw == tot // 2:
          return True
      subs.update(nx)
    return False


print(Solution().canPartition([1, 5, 11, 5]))
