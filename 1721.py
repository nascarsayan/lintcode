class Solution:
  """
  @param S: the given string
  @return: the minimum number of parentheses we must add
  """

  def minAddToMakeValid(self, S):
    # Write your code here
    cnt, op, mp = 0, 0, {'(': 1, ')': -1}
    for c in S:
      op += mp[c]
      if op < 0:
        cnt += 1
        op = 0
    cnt += op
    return cnt


print(Solution().minAddToMakeValid('()))(('))
