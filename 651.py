from collections import defaultdict, deque
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
  """
    @param root: the root of tree
    @return: the vertical order traversal
    """

  def verticalOrder(self, root):
    # write your code here
    lev2val = defaultdict(list)

    que = deque([(root, 0)])
    while (que):
      node, lev = que.popleft()
      if not node:
        continue
      lev2val[lev].append(node.val)
      que.append((node.left, lev - 1))
      que.append((node.right, lev + 1))

    return [lev2val[k] for k in sorted(lev2val.keys())]
