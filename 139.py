class Solution:
  """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

  def subarraySumClosest(self, nums):
    # write your code here
    size = len(nums)
    pre = nums[:]
    for i in range(1, size):
      pre[i] += pre[i - 1]
    tots = list(sorted([(0, -1)] + [(v, i) for i, v in enumerate(pre)]))
    return (min(
        list(
            map(
                lambda x: [
                    abs(x[0][0] - x[1][0]),
                    min(x[0][1], x[1][1]) + 1,
                    max(x[0][1], x[1][1])
                ], zip(tots, tots[1:])))))[1:]


print(Solution().subarraySumClosest([-3, 1, 1, -3, 5]))
