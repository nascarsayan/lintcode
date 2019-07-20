# https://www.lintcode.com/problem/subsets/

class Solution:
  """
  @param nums: A set of numbers
  @return: A list of lists
  """
  def subsets(self, nums):
    # write your code here
    powset = [[]]
    nums.sort()
    for num in nums:
      for i in range(len(powset)):
        powset.append(powset[i] + [num])
    return powset

# print(Solution().subsets([1,2,3]))
