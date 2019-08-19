class Solution:
  """
  @param fronts:
  @param backs:
  @return: nothing
  """

  def flipgame(self, fronts, backs):
    inf = float('inf')
    mn = inf
    same = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
    for num in fronts + backs:
      if num not in same:
        mn = min(mn, num)
    return (mn, 0)[mn == inf]
