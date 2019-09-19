class UniNode:

  def __init__(self, parent, rank):
    self.parent, self.rank = parent, rank


class ConnectingGraph3:

  def __init__(self, n):
    self.sets = [None] + [UniNode(i, 0) for i in range(1, n + 1)]
    self.comps = n

  def find(self, u):
    if self.sets[u].parent != u:
      self.sets[u].parent = self.find(self.sets[u].parent)
    return self.sets[u].parent

  def union(self, u, v):
    if self.sets[u].rank > self.sets[v].rank:
      self.sets[v].parent = u
    elif self.sets[u].rank < self.sets[v].rank:
      self.sets[u].parent = v
    else:
      self.sets[v].parent = u
      self.sets[u].rank += 1

  """
  @param a: An integer
  @param b: An integer
  @return: nothing
  """

  def connect(self, a, b):
    # write your code here
    apar = self.find(a)
    bpar = self.find(b)
    if apar != bpar:
      self.union(apar, bpar)
      self.comps -= 1

  """
  @return: An integer
  """

  def query(self):
    # write your code here
    return self.comps
