class Solution:
  """
  @param bottom: a string
  @param allowed: a list of strings
  @return: return a boolean
  """

  def pyramidTransition(self, bottom, allowed):
    # write your code here
    trie = {}
    for eall in allowed:
      curr = trie
      for ch in eall:
        if ch not in curr:
          curr[ch] = {}
        curr = curr[ch]

    def recurse(path, idx, size):
      if idx == size:
        nst.append(path)
        return
      for ch in chil[idx]:
        recurse(path + ch, idx + 1, size)

    stac = [bottom]
    while (len(stac[0]) > 1):
      nst = []
      size = len(stac[0])
      for est in stac:
        chil = []
        ok = True
        for idx in range(size - 1):
          try:
            chil.append(trie[est[idx]][est[idx + 1]].keys())
          except KeyError:
            ok = False
        if not ok:
          continue
        recurse('', 0, size - 1)
      if len(nst) == 0:
        return False
      stac = nst
    return True


print(Solution().pyramidTransition(
    "ABCD", ["BCE", "BCF", "ABA", "CDA", "AEG", "FAG", "GGG"]))
