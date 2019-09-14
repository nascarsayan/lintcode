class Solution:
  """
  @param nums:
  @return: the maximum result of ai XOR aj, where 0 <= i, j < n
  """

  def findMaximumXOR(self, nums):
    # Write your code here
    res = 0
    for i in range(32)[::-1]:
      res <<= 1
      pre = {num >> i for num in nums}
      res += any(res ^ 1 ^ p in pre for p in pre)
    return res


print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))

# !TLE
# class NNode:

#   def __init__(self, val):
#     self.neigh = {}
#     self.sval = val
#     self.num = None

# class TTrie:

#   def __init__(self):
#     self.root = NNode(None)

#   def insert(self, sval, ival):
#     curr = self.root
#     for c in sval:
#       if c not in curr.neigh:
#         curr.neigh[c] = NNode(c)
#       curr = curr.neigh[c]
#     curr.num = ival

#   def invfind(self, sval, ival):
#     curr = self.root
#     inv = {'0': '1', '1': '0'}
#     for c in sval:
#       if inv[c] in curr.neigh:
#         curr = curr.neigh[inv[c]]
#       else:
#         curr = curr.neigh[c]
#     return int(sval, 2) ^ curr.num

# class Solution:
#   """
#   @param nums:
#   @return: the maximum result of ai XOR aj, where 0 <= i, j < n
#   """

#   def findMaximumXOR(self, nums):
#     # Write your code here
#     strnums = list(map(lambda x: '{:032b}'.format(x), nums))
#     size = len(nums)
#     if size < 2:
#       return 0
#     trie = TTrie()
#     for i, num in enumerate(strnums):
#       trie.insert(num, nums[i])
#     best = 0
#     for i, num in enumerate(strnums):
#       best = max(best, trie.invfind(num, nums[i]))
#     return best
