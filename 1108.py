from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

  def findDuplicateSubtrees(self, root):
    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """
    cnt = defaultdict(list)

    def serial(root):
      if root is None:
        return '#'
      return str(root.val) + ',' + serial(root.left) + ',' + serial(root.right)

    def recurse(root):
      if root is None:
        return
      cnt[serial(root)].append(root)
      recurse(root.left)
      recurse(root.right)

    res = []
    recurse(root)
    for k in cnt:
      if len(cnt[k]) > 1:
        res.append(cnt[k][0])
    return res
