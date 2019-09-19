class MapSum:

  def trienode(self):
    return {'nei': {}, 'val': 0}

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.trie = self.trienode()

  def insert(self, key, val):
    """
    :type key: str
    :type val: int
    :rtype: void
    """
    curr = self.trie
    for c in key:
      if c not in curr['nei']:
        curr['nei'][c] = self.trienode()
      curr = curr['nei'][c]
    curr['val'] = val

  def sum(self, prefix):
    """
    :type prefix: str
    :rtype: int
    """

    def dfs(curr):
      res[0] += curr['val']
      for k in curr['nei']:
        dfs(curr['nei'][k])

    curr = self.trie
    try:
      for c in prefix:
        curr = curr['nei'][c]
      res = [0]
      dfs(curr)
      return res[0]
    except KeyError:
      return 0


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
