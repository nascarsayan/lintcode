class Solution:
  """
  @param nums: a sorted array
  @param a:
  @param b:
  @param c:
  @return: a sorted array
  """

  def sortTransformedArray(self, nums, a, b, c):
    # Write your code here
    def f(x):
      return a * (x**2) + b * x + c

    size = len(nums)
    st, fl = 0, size - 1
    res = []
    sgn = (-1, 1)[a >= 0]
    while (st <= fl):
      fst = f(nums[st])
      ffl = f(nums[fl])
      if (fst - ffl) * sgn >= 0:
        res.append(fst)
        st += 1
      else:
        res.append(ffl)
        fl -= 1
    if a >= 0:
      res = list(reversed(res))
    return res


print(Solution().sortTransformedArray([-4, -2, 2, 4], 0, -1, 5))
