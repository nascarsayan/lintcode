class Solution:
  """
  @param nums: an array
  @return: the minimum number of moves required to make all array elements equal
  """

  def minMoves2(self, nums):
    # Write your code here
    size = len(nums)
    if size < 2:
      return 0
    nums.sort()
    md1 = nums[size // 2]
    md2 = nums[size // 2 - 1]
    return min(
        sum(list(map(lambda x: abs(x - md1), nums))),
        sum(list(map(lambda x: abs(x - (md2 + 1)), nums))))


print(Solution().minMoves2([0, 0, 1, 6, 8]))
