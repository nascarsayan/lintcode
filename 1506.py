"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
    @param root: the root of the tree
    @param target: the target
    @param K: the given K
    @return: All Nodes Distance K in Binary Tree
    """

  def distanceK(self, root, target, K):
    # Write your code here
    def setpar(root, par):
      if root is None:
        return
      root.par = par
      setpar(root.left, root)
      setpar(root.right, root)

    setpar(root, None)
    que = [(target, 0)]
    visited = set()
    while (len(que) > 0 and que[0][1] < K):
      node, dist = que.pop(0)
      visited.add(node)
      for nex in [node.par, node.left, node.right]:
        if nex is not None and nex not in visited:
          que.append((nex, dist + 1))

    return list(map(lambda x: x[0].val, que))
