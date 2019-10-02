class Solution:
  """
  @param a: the given number a
  @param b: the given array
  @return: the result
  """

  def superPow(self, a, b):
    # Write your code here
    PR = 1337
    dp = {}
    a = a % PR

    def poww(b):
      if b in dp:
        return dp[b]
      if b < 2:
        dp[b] = (a**b) % PR
      else:
        dp[b] = (poww(b // 2) * poww(b - b // 2)) % PR
      return dp[b]

    return poww(int(''.join(list(map(str, b)))))


print(Solution().superPow(2, [1, 0]))
