"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class ListNode(object):

  def __init__(self, val, next=None):
    self.val = val
    self.next = next


class Solution:
  """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

  def rehashing(self, hashTable):
    # write your code here
    size = len(hashTable) * 2
    if size == 0:
      return hashTable
    newt = [ListNode(None) for _ in range(size)]
    currt = newt[:]
    for iold in range(size // 2):
      ptr = hashTable[iold]
      while (ptr):
        val = ptr.val
        inew = val % size
        currt[inew].next = ListNode(val)
        currt[inew] = currt[inew].next
        ptr = ptr.next
    return list(map(lambda x: x.next, newt))
