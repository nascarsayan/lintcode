from functools import cmp_to_key


class Solution:
  """
    @param nums: A list of non negative integers
    @return: A string
    """

  def largestNumber(self, nums):
    # write your code here
    maxnum = ''

    def comp(x, y):
      stx = str(x)
      sty = str(y)
      s1 = stx + sty
      s2 = sty + stx
      if (s1 > s2):
        return -1
      elif (s1 < s2):
        return 1
      else:
        return 0

    nums.sort(key=cmp_to_key(comp))
    for num in nums:
      maxnum += str(num)
    return str(int(maxnum))


# print(Solution().largestNumber([4, 6, 65]))
