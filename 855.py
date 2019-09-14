class SetNode:

  def __init__(self, parent, rank):
    self.parent, self.rank = parent, rank

  def __repr__(self):
    return 'p :{}, r: {}'.format(self.parent, self.rank)


class Solution:
  """
  @param words1:
  @param words2:
  @param pairs:
  @return: Whether sentences are similary or not?
  """

  def areSentencesSimilarTwo(self, words1, words2, pairs):
    #
    def find(u):
      if sets[u].parent != u:
        sets[u].parent = find(sets[u].parent)
      return sets[u].parent

    def union(u, v):
      if sets[u].rank > sets[v].rank:
        sets[v].parent = u
      elif sets[u].rank < sets[v].rank:
        sets[u].parent = v
      else:
        sets[v].parent = u
        sets[u].rank += 1

    w2idx = {}
    sets = []
    for u, v in pairs:
      if u not in w2idx:
        w2idx[u] = len(sets)
        sets.append(SetNode(w2idx[u], 0))
      if v not in w2idx:
        w2idx[v] = len(sets)
        sets.append(SetNode(w2idx[v], 0))
      u_par = find(w2idx[u])
      v_par = find(w2idx[v])
      union(u_par, v_par)
    for u, v in zip(words1, words2):
      if u == v:
        continue
      try:
        if find(w2idx[u]) != find(w2idx[v]):
          return False
      except:
        return False
    return True


print(Solution().areSentencesSimilarTwo(
    ["great", "acting", "skills"], ["fine", "drama", "talent"],
    [["great", "good"], ["fine", "good"], ["drama", "acting"],
     ["skills", "talent"]]))
