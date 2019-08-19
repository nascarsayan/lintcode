# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
  """
  @param graph: a list of Undirected graph node
  @param A: nodeA
  @param B: nodeB
  @return:  the length of the shortest path
  """

  def shortestPath(self, graph, A, B):
    # Write your code here
    que = [(A, 0)]
    while (len(que) > 0):
      node, d = que.pop(0)
      if id(node) == id(B):
        return d
      for nei in node.neighbors:
        que.append((nei, d + 1))
    return -1
