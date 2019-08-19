# Check out CPP
# class Solution:
#   """
#   @param n: An integer
#   @param m: An integer
#   @param i: A bit position
#   @param j: A bit position
#   @return: An integer
#   """

#   def updateBits(self, n, m, i, j):
#     # write your code here
#     mask = None
#     if j < 31:
#       mask = ~((1 << j + 1) - (1 << i))
#     else:
#       mask = (1 << i) - 1
#     return (n & mask) + (m << i)
