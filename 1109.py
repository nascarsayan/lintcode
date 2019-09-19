class Solution:
  """
  @param senate: a string
  @return: return a string
  """

  def predictPartyVictory(self, senate):
    # write your code here
    mp = {'R': 'Radiant', 'D': 'Dire'}
    stac = [[senate[0], 0]]
    for nex in senate[1:]:
      pre, hit = stac[-1]
      if pre == nex:
        stac.append([nex, 0])
      else:
        if hit == 0:
          stac[-1][1] = 1
        else:
          stac.pop(-1)
          if len(stac) == 0:
            stac.append([nex, 1])
    return mp[stac[0][0]]


print(Solution().predictPartyVictory('RDRDRDDDD'))
