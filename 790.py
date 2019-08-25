from collections import defaultdict

class Solution:
  """
  @param generator: Generating set of rules.
  @param startSymbol: Start symbol.
  @param symbolString: Symbol string.
  @return: Return true if the symbol string can be generated, otherwise return false.
  """

  def canBeGenerated(self, generator, startSymbol, symbolString):
    # Write  your code here.
    def isgen(curr, size):
      if len(curr) > size:
        return False
      newc = ''
      for i in range(len(curr)):
        if 'a' <= curr[i] <= 'z':
          newc += curr[i]
        else:
          newc += 


    gens = defaultdict(list)
    for gen in generator:
      lt, rt = gen.split(' -> ')
      gens[lt].append(rt)
    return isgen(startSymbol, len(symbolString))
