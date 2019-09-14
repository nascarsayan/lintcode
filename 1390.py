class Solution:
  """
  @param words:
  @return: nothing
  """

  def minimumLengthEncoding(self, words):
    #
    def recurse(curr, d):
      if len(curr['nei'].keys()) == 0:
        tot[0] += d
        return
      for ch in curr['nei']:
        recurse(curr['nei'][ch], d + 1)

    def trienode():
      return {'nei': {}, 'end': False}

    trie = trienode()
    for word in words:
      curr = trie
      for c in word[::-1]:
        if c not in curr['nei']:
          curr['nei'][c] = trienode()
        curr = curr['nei'][c]
      curr['end'] = True
    tot = [0]
    recurse(trie, 1)
    return tot[0]
