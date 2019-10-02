class Solution:
  """
  @param A: A string
  @param B: A string
  @return: The length of longest common subsequence of A and B
  """

  def longestCommonSubsequence(self, A, B):
    # write your code here
    la, lb = len(A), len(B)
    dp = [0] * (lb + 1)
    for ir in range(la):
      dp2 = [0] * (lb + 1)
      for ic in range(1, lb + 1):
        if A[ir] == B[ic - 1]:
          dp2[ic] = dp[ic - 1] + 1
        else:
          dp2[ic] = max(dp2[ic - 1], dp[ic])
      dp = dp2
    return dp[-1]


print(Solution().longestCommonSubsequence('ABCD', 'EDCA'))
