from collections import defaultdict


class UniNode:

  def __init__(self, parent, rank):
    self.parent, self.rank = parent, rank


class Solution:
  """
  @param accounts: List[List[str]]
  @return: return a List[List[str]]
  """

  def accountsMerge(self, accounts):
    # write your code here
    def find(u):
      if sets[u].parent != u:
        sets[u].parent = find(sets[u].parent)
      return sets[u].parent

    def union(u, v):
      if sets[u].rank < sets[v].rank:
        sets[v].parent = u
      elif sets[u].rank > sets[v].rank:
        sets[u].parent = v
      else:
        sets[v].parent = u
        sets[u].rank += 1

    idcs = defaultdict(set)
    size = len(accounts)
    sets = [UniNode(i, 0) for i in range(size)]
    for idx, acc in enumerate(accounts):
      for email in acc[1:]:
        idcs[email].add(idx)
    for commu in [list(x) for x in idcs.values()]:
      if len(commu) == 1:
        continue
      upar = find(commu[0])
      for v in commu[1:]:
        vpar = find(v)
        union(upar, vpar)
    uniq = defaultdict(set)
    for u, acc in enumerate(accounts):
      upar = find(u)
      uniq[upar].update(acc[1:])
    res = []
    for k in uniq:
      res.append([accounts[k][0]] + list(sorted(list(uniq[k]))))

    return res


print(Solution().accountsMerge(
    [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
     ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
