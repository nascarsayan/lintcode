class Solution:
  """
  @param nums: the given array
  @return:  the number of triplets chosen from the array that can make triangles
  """

  def triangleNumber(self, nums):
    # Write your code here
    nums.sort()
    size, res = len(nums), 0
    for i3 in range(2, size)[::-1]:
      i1, i2 = 0, i3 - 1
      while (i1 < i2):
        while (i1 < i2 and nums[i1] + nums[i2] <= nums[i3]):
          i1 += 1
        res += i2 - i1
        i2 -= 1
    return res


print(Solution().triangleNumber([2, 6, 6, 7, 7, 8, 8, 9]))
