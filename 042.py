class Solution:
  """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

  def maxTwoSubArrays(self, nums):
    # write your code here
    ninf = float('-inf')
    l = len(nums)
    maxLeft = [ninf] * l
    maxRight = [ninf] * l

    sumL = sumR = 0
    for i in range(l):
      sumL += nums[i]
      sumR += nums[l - i - 1]
      maxLeft[i] = sumL
      maxRight[l - i - 1] = sumR
      if i > 0:
        maxLeft[i] = max(maxLeft[i], maxLeft[i - 1])
        maxRight[l - i - 1] = max(maxRight[l - i - 1], maxRight[l - i])
      if sumL < 0:
        sumL = 0
      if sumR < 0:
        sumR = 0
    maxSum = ninf
    for i in range(l - 1):
      maxSum = max(maxSum, maxLeft[i] + maxRight[i + 1])
    return maxSum


# print(Solution().maxTwoSubArrays([1, 3, -1, 2, -1, 2]))
