class Solution:
  """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

  def numDecodings(self, s):
    # write your code here
    size = len(s)
    if size == 0 or s[0] == '0':
      return 0
    for c in s:
      if not (c >= '0' and c <= '9'):
        return 0
    dp = [0] * (size + 1)
    dp[0] = dp[1] = 1
    for idx in range(1, size):
      cnt = 0
      if s[idx] != '0':
        cnt += dp[idx]
      code = int(s[idx - 1:idx + 1])
      if code > 9 and code <= 26:
        cnt += dp[idx - 1]
      dp[idx + 1] = cnt
    print(dp)
    return dp[size]


# print(Solution().numDecodings('123'))
