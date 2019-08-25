"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import json


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
    que = []
    que.append(root)
    ser = []
    while (len(que) > 0):
      node = que.pop(0)
      if node is None:
        ser.append('#')
      else:
        ser.append(str(node.val))
        que.append(node.left)
        que.append(node.right)
    return json.dumps(ser)

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
    ser = json.loads(data)
    if ser[0] == '#':
      return None
    root = TreeNode(int(ser[0]))
    que = [root]
    ser.pop(0)
    while (len(ser) > 0):
      node = que.pop(0)
      lt = ser.pop(0)
      rt = ser.pop(0)
      if lt.isdigit():
        node.left = TreeNode(int(lt))
        que.append(node.left)
      if rt.isdigit():
        node.right = TreeNode(int(rt))
        que.append(node.right)
    return root
