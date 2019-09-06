class Solution:
  """
  @param S: a string
  @return: return a string
  """

  def makeLargestSpecial(self, S):
    # write your code here
    count = i = 0
    res = []
    for j, v in enumerate(S):
      count = count + 1 if v == '1' else count - 1
      if count == 0:
        res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
        i = j + 1
    return ''.join(sorted(res)[::-1])


print(Solution().makeLargestSpecial('11011000'))
