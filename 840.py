class SegTreeNode:

  def __init__(self, li, ri):
    self.li, self.ri = li, ri
    self.tot = 0
    self.left, self.right = None, None


class NumArray:

  def __init__(self, nums):
    """
    :type nums: List[int]
    """

    def recurse(li, ri):
      if li > ri:
        return 0
      root = SegTreeNode(li, ri)
      if li == ri:
        root.tot = nums[li]
        return root
      mid = (li + ri) >> 1
      root.left = recurse(li, mid)
      root.right = recurse(mid + 1, ri)
      root.tot = root.left.tot + root.right.tot
      return root

    self.root = recurse(0, len(nums) - 1)
    self.nums = nums

  def update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: void
    """

    def recurse(root):
      if root is None:
        return
      if root.li <= i <= root.ri:
        root.tot += val - self.nums[i]
        recurse(root.left)
        recurse(root.right)

    recurse(self.root)
    self.nums[i] = val

  def sumRange(self, i, j):
    """
    :type i: int
    :type j: int
    :rtype: int
    """

    def recurse(root):
      if root is None:
        return 0
      if max(root.li, i) > min(root.ri, j):
        return 0
      if root.li >= i and root.ri <= j:
        return root.tot
      return recurse(root.left) + recurse(root.right)

    return recurse(self.root)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
