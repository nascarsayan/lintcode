class Solution:
  """
  @param preorder: a string
  @return: return a bool
  """

  def isValidSerialization(self, preorder):
    # write your code here
    def recurse():
      if idx[0] == size:
        return False
      idx[0] = idx[0] + 1
      if preorder[idx[0] - 1] == '#':
        return True
      if not recurse():
        return False
      return recurse()

    preorder = preorder.split(',')
    size = len(preorder)
    idx = [0]
    if not recurse():
      return False
    return idx[0] == size
