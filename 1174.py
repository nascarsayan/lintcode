class Solution:
  """
  @param n: an integer
  @return: the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n
  """

  def nextGreaterElement(self, n):
    # Write your code here
    INT_MAX = 2**31 - 1
    nums = list(map(int, str(n)))
    size = len(nums)
    i = size - 2
    while (i >= 0 and nums[i] >= nums[i + 1]):
      i -= 1
    if i == -1:
      return -1
    j = i + 1
    while (j < size and nums[j] > nums[i]):
      j += 1
    nums[i], nums[j - 1] = nums[j - 1], nums[i]
    nums = nums[:i + 1] + sorted(nums[i + 1:])
    v = int(''.join(list(map(str, nums))))
    if v <= INT_MAX:
      return v
    return -1


print(Solution().nextGreaterElement(19999999999))
