class Solution:
  """
  @param N: N
  @return: return the number of distinct numbers can you dial in this manner mod 1e9+7
  """

  def knightDialer(self, N):
    #
    PR = 1000000007
    graph = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    dp = [1] * 10
    for _ in range(1, N):
      dp2 = [0] * 10
      for dig in range(10):
        for nei in graph[dig]:
          dp2[dig] += dp[nei]
        dp2[dig] = dp2[dig] % PR
      dp = dp2
    return sum(dp) % PR
