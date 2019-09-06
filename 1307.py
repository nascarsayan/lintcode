class Solution:
  """
  @param preo: List[int]
  @return: return a boolean
  """

  def verifyPreorder(self, preo):
    # write your code here
    stac, root = [], float('-inf')
    for node in preo:
      if node < root:
        return False
      while (len(stac) > 0 and stac[-1] < node):
        root = stac.pop(-1)
      stac.append(node)
    return True


# !TLE
# def verifyPreorder(self, preo):
#   # write your code here
#   def feas(st, fl):
#     if st > fl:
#       return True
#     try:
#       idx = ino.index(preo[ptr[0]], st, fl + 1)
#       ptr[0] += 1
#       return feas(st, idx - 1) and feas(idx + 1, fl)
#     except:
#       return False

#   ino = list(sorted(preo[:]))
#   ptr = [0]
#   size = len(ino)
#   return feas(0, size - 1)
