"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """

  def findClosestLeaf(self, root, k):
    # Write your code here
    def setpar(root, par):
      if root is None:
        return
      root.par = par
      setpar(root.left, root)
      setpar(root.right, root)

    def getkn(root):
      if root is None:
        return None
      if root.val == k:
        return root
      lef = getkn(root.left)
      if lef is not None:
        return lef
      return getkn(root.right)

    setpar(root, None)
    kn = getkn(root)
    if kn.left is None and kn.right is None:
      return kn.val
    que = [x for x in [kn.left, kn.right, kn.par] if x is not None]
    visited = set(que + [kn])
    while True:
      node = que.pop(0)
      visited.add(node)
      if node.left is None and node.right is None:
        return node.val
      for nnode in [node.left, node.right, node.par]:
        if nnode is not None and nnode not in visited:
          que.append(nnode)


# !TLE
# def findClosestLeaf(self, root, k):
#   # Write your code here
#   def setpar(root, par):
#     if root is None:
#       return
#     root.par = par
#     setpar(root.left, root)
#     setpar(root.right, root)

#   def getkn(root):
#     if root is None:
#       return None
#     if root.val == k:
#       return root
#     lef = getkn(root.left)
#     if lef is not None:
#       return lef
#     return getkn(root.right)

#   setpar(root, None)
#   kn = getkn(root)
#   if kn.left is None and kn.right is None:
#     return kn.val
#   que = [x for x in [kn.left, kn.right, kn.par] if x is not None]
#   visited = set(que + [kn])
#   while True:
#     node = que.pop(0)
#     if node.left is None and node.right is None:
#       return node.val
#     for nnode in [node.left, node.right, node.par]:
#       if nnode is not None and nnode not in visited:
#         que.append(nnode)
