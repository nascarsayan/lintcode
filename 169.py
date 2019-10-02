class Solution:
  """
  @param n: the number of disks
  @return: the order of moves
  """

  def towerOfHanoi(self, n):
    # write your code here
    dp = {}

    def recurse(n, st, fl, mid):
      if (n, st, fl) in dp:
        return dp[(n, st, fl)]
      dp[(n, st, fl)] = ['from %s to %s' % (st, fl)]
      if n > 1:
        dp[(n, st, fl)] = recurse(
            n - 1, st, mid, fl) + dp[(n, st, fl)] + recurse(n - 1, mid, fl, st)
      return dp[(n, st, fl)]

    if n < 1:
      return []
    return recurse(n, 'A', 'C', 'B')


print(Solution().towerOfHanoi(3))
