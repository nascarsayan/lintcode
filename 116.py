class Solution:
  """
    @param A: A list of integers
    @return: A boolean
    """

  def canJump(self, A):
    # write your code here
    size = len(A)
    dp = [False] * size
    dp[-1] = True
    for st in range(size - 2, -1, -1):
      if A[st] >= size - 1 - st:
        dp[st] = True
        continue
      for nex in range(st + 1, min(st + A[st] + 1, size - 1)):
        if dp[nex]:
          dp[st] = True
          break
    return dp[0]


# print(Solution().canJump([2, 3, 1, 1, 4]))
