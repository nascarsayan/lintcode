class Solution:
  """
  @param S: a string
  @param words: a dictionary of words
  @return: the number of words[i] that is a subsequence of S
  """

  def numMatchingSubseq(self, S, words):
    # Write your code here
    def trienode():
      return {'n': {}, 'w': 0, 'v': False}

    trie = trienode()
    for word in words:
      curr = trie
      for c in word:
        if c not in curr['n']:
          curr['n'][c] = trienode()
        curr = curr['n'][c]
      curr['w'] += 1
    trie['v'] = True
    tree, tot = [trie], 0
    for c in S:
      nex = []
      for node in tree:
        if c in node['n'] and not node['n'][c]['v']:
          nex.append(node['n'][c])
          tot += node['n'][c]['w']
          node['n'][c]['v'] = True
      tree.extend(nex)
    return tot


print(Solution().numMatchingSubseq('abcde', ["a", "bb", "acd", "ace"]))
