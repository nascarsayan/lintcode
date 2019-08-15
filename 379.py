from functools import cmp_to_key


class Solution:
  """
    @param nums: n non-negative integer array
    @return: A string
    """

  def minNumber(self, nums):
    # write your code here
    def mycmp(n1, n2):
      return (1, -1)[n1 + n2 < n2 + n1]

    nums = [str(num) for num in nums]
    nums.sort(key=cmp_to_key(mycmp))
    s = ''.join(nums).lstrip('0')
    s = (s, '0')[len(s) == 0]
    return s
