class Solution:
  """
  @param S: A string
  @param T: A string
  @return: Count the number of distinct subsequences
  """

  def numDistinct(self, S, T):
    # write your code here
    ls, lt = len(S), len(T)
    if ls < lt:
      return 0
    dp1 = [1] * (ls + 1)
    for ir in range(1, lt + 1):
      dp2 = [0] * (ls + 1)
      for ic in range(ir, ls + 1):
        dp2[ic] = dp2[ic - 1]
        if S[ic - 1] == T[ir - 1]:
          dp2[ic] += dp1[ic - 1]
      dp1 = dp2
    return dp1[-1]


print(Solution().numDistinct('rabbbit', 'rabbit'))
