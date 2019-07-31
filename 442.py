class Trie:

  def __init__(self):
    # do intialization if necessary
    self.trie = {}

  """
    @param: word: a word
    @return: nothing
    """

  def insert(self, word):
    # write your code here
    curr = self.trie
    for c in word:
      if c not in curr:
        curr[c] = {}
      curr = curr[c]
    curr['pr'] = True

  """
    @param: word: A string
    @return: if the word is in the trie.
    """

  def search(self, word):
    # write your code here
    curr = self.trie
    for c in word:
      if c not in curr:
        return False
      curr = curr[c]
    if 'pr' in curr and curr['pr']:
      return True
    return False

  """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

  def startsWith(self, prefix):
    # write your code here
    curr = self.trie
    for c in prefix:
      if c not in curr:
        return False
      curr = curr[c]
    return True
