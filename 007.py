# https://www.lintcode.com/problem/serialize-and-deserialize-binary-tree/
# TODO deserialize
# ! easier to do it in C++

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
  """
  @param root: An object of TreeNode, denote the root of the binary tree.
  This method will be invoked first, you should design your own algorithm 
  to serialize a binary tree which denote by a root node to a string which
  can be easily deserialized by your own "deserialize" method later.
  """
  def serialize(self, root):
    # write your code here
    if (root is None):
      return '#'
    return str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)

  """
  @param data: A string serialized by your serialize method.
  This method will be invoked second, the argument data is what exactly
  you serialized at method "serialize", that means the data is not given by
  system, it's given by your own serialize method. So the format of data is
  designed by yourself, and deserialize it here as you serialize it in 
  "serialize" method.
  """
  def deserialize(self, data):
    # write your code here
    def deserHelp(arrp, treep):
      v = arrp[0].pop(0)
      if (v == '#'):
        return
      treep[0] = TreeNode(int(v))
      deserHelp(arrp, treep[0].left)
      deserHelp(arrp, treep[0].right)

    aug = [None]
    deserHelp([data.split()], aug)
    return aug[0]

# {3,9,20,#,#,15,7}
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)
print(Solution().deserialize(Solution().serialize(root)))