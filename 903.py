class MySeg:

  def __init__(self, st, fl):
    self.st, self.fl, self.cnt = st, fl, 0
    self.left, self.right = None, None


class Solution:
  """
  @param length: the length of the array
  @param updates: update operations
  @return: the modified array after all k operations were executed
  """

  def getModifiedArray(self, length, updates):
    # Write your code here
    if length == 0:
      return []
    dif = [0] * (length + 1)
    res = [0] * length
    for st, fl, inc in updates:
      dif[st] += inc
      dif[fl + 1] -= inc
    res[0] = dif[0]
    for idx in range(1, length):
      res[idx] = res[idx - 1] + dif[idx]
    return res


# !TLE

# def getModifiedArray(self, length, updates):
#   # Write your code here
#   def getroot(st, fl):
#     if st > fl:
#       return None
#     root = MySeg(st, fl)
#     if st == fl:
#       return root
#     mid = (st + fl) >> 1
#     root.left = getroot(st, mid)
#     root.right = getroot(mid + 1, fl)
#     return root

#   def inc(root, update):
#     if root is None:
#       return
#     if root.st >= update[0] and root.fl <= update[1]:
#       root.cnt += update[2]
#       return
#     inc(root.left, update)
#     inc(root.right, update)

#   def getres(root, psum):
#     psum += root.cnt
#     if all(x is None for x in [root.left, root.right]):
#       arr.append(psum)
#       return
#     getres(root.left, psum)
#     getres(root.right, psum)

#   if length == 0:
#     return []
#   root = getroot(0, length - 1)
#   for update in updates:
#     inc(root, update)
#   arr = []
#   getres(root, 0)
#   return arr
