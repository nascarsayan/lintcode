class Solution:
  """
  @param N: int
  @param K: int
  @param W: int
  @return: the probability
  """

  def new21Game(self, N, K, W):
    # Write your code here.
    if K == 0 or N >= K + W:
      return 1
    dp, tot = [1] + [0] * N, 1
    for i in range(1, N + 1):
      dp[i] = tot / W
      if i < K:
        tot += dp[i]
      if i >= W:
        tot -= dp[i - W]
    return sum(dp[K:])
