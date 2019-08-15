from functools import cmp_to_key


class Solution:
  """
  @param S: a string
  @return: return a string
  """

  def makeLargestSpecial(self, S):
    # write your code here
    def mycmp(s1, s2):
      return int(s2) - int(s1)

    size = len(S)
    invs = []
    dif = 0
    curv = []
    for i in range(size):
      dif += 2 * int(S[i]) - 1
      if dif < 0:
        if len(curv) > 0:
          invs.append(curv)
          curv = []
        dif = 0
      elif len(curv) == 0 or dif == 0:
        curv.append(i)
    if len(curv) > 0:
      invs.append(curv)
    if len(invs) == 0:
      return S
    invs.append([len(S)])
    maxs = S[:invs[0][0]]
    for i in range(len(invs) - 1):
      invisize = len(invs[i])
      if invisize < 3:
        maxs += S[invs[i][0]:invs[i + 1][0]]
      else:
        subs = [S[invs[i][j]:invs[i][j + 1] + 1] for j in range(invisize - 1)]
        subs.sort(key=cmp_to_key(mycmp))
        maxs += ''.join(subs) + S[invs[i][invisize - 1] + 1:invs[i + 1][0]]
    return maxs


print(Solution().makeLargestSpecial('1001100101100'))
