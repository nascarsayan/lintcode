class Solution:
  """
  @param nums: the array
  @return: the minimum times to flip digit
  """

  def flipDigit(self, nums):
    # Write your code here
    zero, one = 0, 0
    for num in nums:
      zero = min(zero, one) + num
      one = one + (num ^ 1)
    return min(zero, one)
