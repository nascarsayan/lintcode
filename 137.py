from collections import defaultdict
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class UndirectedGraphNode:

  def __init__(self, x):
    self.label = x
    self.neighbors = []


class Solution:

  def __init__(self):
    self.nodemap = defaultdict(UndirectedGraphNode)

  def recurse(self, curr, newcurr, visited):
    idcurr = id(curr)
    if curr is None or idcurr in visited:
      return
    visited.add(idcurr)
    for idx, nei in enumerate(curr.neighbors):
      if nei is None:
        continue
      idnei = id(nei)
      if idnei not in self.nodemap:
        self.nodemap[idnei] = UndirectedGraphNode(nei.label)
      newcurr.neighbors.append(self.nodemap[idnei])
    for idx in range(len(curr.neighbors)):
      self.recurse(curr.neighbors[idx], newcurr.neighbors[idx], visited)

  """
  @param: head: A undirected graph node
  @return: A undirected graph node
  """

  def cloneGraph(self, head):
    # write your code here
    if head is None:
      return head
    newhead = UndirectedGraphNode(head.label)
    visited = set()
    self.nodemap[id(head)] = newhead
    self.recurse(head, newhead, visited)
    return newhead


# one = UndirectedGraphNode(1)
# two = UndirectedGraphNode(2)
# three = UndirectedGraphNode(3)

# one.neighbors = [two, three]
# two.neighbors = [one, three]
# three.neighbors = [two, one]

# Solution().cloneGraph(one)
