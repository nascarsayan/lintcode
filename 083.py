class Solution:
  """
    @param A: An integer array
    @return: An integer
    """

  def singleNumberII(self, A):
    # write your code here
    one = two = 0
    for a in A:
      # s1 -> why this kolaveri di?
      # one = (one ^ a) & ~two
      # two = (two ^ a) & ~one

      # s2 -> well established
      two = two | (one & a)
      one ^= a
      cbm = ~(one & two)
      one &= cbm
      two &= cbm
    return one


print(Solution().singleNumberII([2, 1, 2, 2]))
