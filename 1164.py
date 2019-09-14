class Solution:
  """
  @param nums: the given sequence
  @return: the length of the longest subsequence that is a wiggle sequence
  """

  def wiggleMaxLength(self, nums):
    # Write your code here
    size = len(nums)
    if size == 0:
      return 0
    inc = [1] * size
    dec = [1] * size
    for i in range(1, size):
      for j in range(i):
        if nums[j] < nums[i]:
          inc[i] = max(inc[i], dec[j] + 1)
        if nums[j] > nums[i]:
          dec[i] = max(dec[i], inc[j] + 1)
    return max(inc + dec)


print(Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]))
