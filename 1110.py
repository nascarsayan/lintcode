class Solution:
  """
  @param dict: List[str]
  @param sentence: a string
  @return: return a string
  """

  def replaceWords(self, dic, sentence):
    # write your code here
    def newn():
      return {'n': {}, 'v': None}

    trie = newn()
    for wd in dic:
      curr = trie
      for ch in wd:
        if ch not in curr['n']:
          curr['n'][ch] = newn()
        curr = curr['n'][ch]
      curr['v'] = wd
    wds = sentence.split(' ')
    for i in range(len(wds)):
      curr = trie
      fl = False
      for c in wds[i]:
        try:
          curr = curr['n'][c]
          if curr['v'] is not None:
            fl = True
            break
        except KeyError:
          break

      if fl:
        wds[i] = curr['v']
    return ' '.join(wds)
