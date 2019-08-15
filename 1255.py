class Solution:
  """
    @param num: a string
    @param k: an integer
    @return: return a string
    """

  def removeKdigits(self, num, k):
    # write your code here
    stac = []
    size = len(num)
    idx = 0
    while (idx < size and k > 0):
      if len(stac) == 0 or num[idx] >= stac[-1]:
        stac.append(num[idx])
        idx += 1
      else:
        stac.pop(-1)
        k -= 1
    while (k > 0):
      stac.pop(-1)
      k -= 1
    ret = (''.join(stac) + num[idx:]).lstrip('0')
    ret = (ret, '0')[len(ret) == 0]
    return ret


print(Solution().removeKdigits('1234567890', 10))
