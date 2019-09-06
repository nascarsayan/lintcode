from collections import defaultdict

class Solution:
  """
  @param n: n nodes labeled from 0 to n - 1
  @param edges: a undirected graph
  @return:  a list of all the MHTs root labels
  """

  def findMinHeightTrees(self, n, edges):
    # Wirte your code here
    def dfs()

    graph = defaultdict(set)
    for u, v in edges:
      graph[u].add(v)
      graph[v].add(u)
    for edge in graph[0]:

