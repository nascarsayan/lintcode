class Solution:
  """
  @param N: an integer
  @return: the probability that soup A will be empty first
  """

  def soupServings(self, N):
    # Write your code here
    if N >= 4800:
      return 1
    dp = {}

    def recurse(a, b):
      if (a, b) in dp:
        return dp[(a, b)]
      if a <= 0 and b <= 0:
        return 0.5
      if a <= 0:
        return 1
      if b <= 0:
        return 0
      dp[(a, b)] = sum(recurse(a - k, b - (4 - k)) for k in [4, 3, 2, 1]) / 4
      return dp[(a, b)]

    n = (N + 24) // 25
    v = recurse(n, n)
    return round(v, 2)


print(Solution().soupServings(50))
