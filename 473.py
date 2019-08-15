class WordDictionary:

  def __init__(self):
    self.trie = {}

  """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

  def addWord(self, word):
    # write your code here
    curr = self.trie
    for c in word:
      if c not in curr:
        curr[c] = {}
      curr = curr[c]
    curr['is'] = True

  """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

  def search(self, word):
    # write your code here
    def recurse(curr, rem):
      try:
        if type(curr) == bool:
          return False
        if rem == '':
          return curr['is']
        if rem[0] == '.':
          if any(recurse(curr[k], rem[1:]) for k in curr):
            return True
          return False
        else:
          return recurse(curr[rem[0]], rem[1:])
      except KeyError:
        return False

    return recurse(self.trie, word)
