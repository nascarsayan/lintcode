class Solution:
  """
  @param nums:  an array of n integers
  @param target: a target
  @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
  """

  def threeSumSmaller(self, nums, target):
    # Write your code here
    size = len(nums)
    if size < 3:
      return 0
    nums.sort()
    tot = 0
    for i in range(size - 2):
      k = size - 1
      for j in range(i + 1, size - 1):
        while (j < k and nums[i] + nums[j] + nums[k] >= target):
          k -= 1
        tot += k - j
        if j == k:
          break
    return tot


print(Solution().threeSumSmaller([1, -2, 2, 1, 0], 1))
