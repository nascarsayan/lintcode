"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class ListNode(object):

  def __init__(self, val, next=None):
    self.val = val
    self.next = next


class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


class Solution:
  """
  @param: head: The first node of linked list.
  @return: a tree node
  """

  def recurse(self, inor):
    size = len(inor)
    if size == 0:
      return None
    mid = size // 2
    root = TreeNode(inor[mid])
    root.left = self.recurse(inor[:mid])
    root.right = self.recurse(inor[mid + 1:])
    return root

  def sortedListToBST(self, head):
    # write your code here
    inor = []
    while (head):
      inor.append(head.val)
      head = head.next
    return self.recurse(inor)
