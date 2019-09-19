class Solution:
  """
  @param nums: an array
  @return: the number of longest increasing subsequence
  """

  def findNumberOfLIS(self, nums):
    # Write your code here
    size = len(nums)
    if size == 0:
      return 0
    lis = [1] * size
    nlis = [0] * size
    for i in range(size):
      for j in range(i):
        if nums[j] < nums[i]:
          lis[i] = max(lis[i], lis[j] + 1)
    for i in range(size):
      if lis[i] == 1:
        nlis[i] = 1
        continue
      for j in range(i):
        if lis[j] == lis[i] - 1 and nums[j] < nums[i]:
          nlis[i] += nlis[j]
    mx = max(lis)
    cnt = 0
    for i in range(size):
      if lis[i] == mx:
        cnt += nlis[i]
    return cnt


print(Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
