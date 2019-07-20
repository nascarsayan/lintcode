# https://www.lintcode.com/problem/dices-sum/
import math

class Solution:
  # @param {int} n an integer
  # @return {tuple[]} a list of tuple(sum, probability)
  def nCr(self, n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

  def dicesSum(self, n):
    # Write your code here
    FACE = 6
    maxSum = FACE * n
    pdist = [None] * (maxSum - n + 1)
    for s in range(n, maxSum + 1):
      times = (s - n) // FACE
      ways = 0
      for k in range(times + 1):
        ways += pow(-1, k) * self.nCr(n, k) * self.nCr(s - FACE * k - 1, s - FACE * k - n)
      pdist[s - n] = [s, ways / pow(FACE, n)]
    return pdist

# print(Solution().dicesSum(2))
