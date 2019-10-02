from collections import deque
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


class Solution:

  def serialize(self, root):
    que = deque([root])
    res = []
    while (que):
      node = que.popleft()
      res.append(str(node.val) if node else '#')
      if node:
        que.extend([node.left, node.right])
    return ','.join(res)

  def deserialize(self, data):
    vals = data.split(',')
    if vals[0] == '#':
      return None
    root = TreeNode(int(vals[0]))
    frontier, ptr = deque([root]), 1
    while (frontier):
      node = frontier.popleft()
      try:
        node.left = TreeNode(int(vals[ptr]))
        frontier.append(node.left)
      except:
        pass
      try:
        node.right = TreeNode(int(vals[ptr + 1]))
        frontier.append(node.right)
      except:
        pass
      ptr += 2
    return root
