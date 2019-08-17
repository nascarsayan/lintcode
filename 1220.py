class Solution:
  """
  @param nums: an array
  @return: whether you could make one square using all the matchsticks the little match girl has
  """

  def makesquare(self, nums):
    # Write your code here
    def recurse(idx, sides):
      if idx == size:
        return all(x == side for x in sides)
      for i in range(4):
        if sides[i] + nums[idx] <= side:
          sides[i] += nums[idx]
          if recurse(idx + 1, sides):
            return True
          sides[i] -= nums[idx]
      return False

    size = len(nums)
    tot = sum(nums)
    if tot == 0:
      return False
    if tot % 4 != 0:
      return False
    side = tot // 4
    sides = [0] * 4
    nums.sort(reverse=True)
    x = recurse(0, sides)
    return x


print(Solution().makesquare([3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
