from functools import cmp_to_key
# * O((n/2)*2^(n/2))


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y


class Solution:

  def getCombination(self, u, i, v, c):
    p = Point(0, 0)
    while (u > 0):
      if (u & 1):
        p.y += v[i]
        p.x += c[i]
      i += 1
      u = u // 2
    return p

  """
  @param s: The capacity of backpack
  @param v: The value of goods
  @param c: The capacity of goods
  @return: The answer
  """

  def getMaxValue(self, s, v, c):
    # Write your code here
    def comp(A, B):
      if (A.x == B.x):
        return A.y - B.y
      else:
        return A.x - B.x

    n = len(v)
    mid = n // 2
    tot = 1 << mid
    ans = 0
    temp, combination = [], []
    for i in range(tot):
      t = self.getCombination(i, 0, v, c)
      temp.append(t)
    temp.sort(key=cmp_to_key(comp))
    maxv = -1
    for i in temp:
      if (i.y > maxv):
        combination.append(i)
        maxv = i.y
    tot = 1 << (n - mid)
    m = len(combination)
    for i in range(tot):
      t = self.getCombination(i, mid, v, c)
      cap = s - t.x
      if (cap > 0):
        left, right = 0, m - 1
        index = -1
        while (left <= right):
          middle = (left + right) // 2
          if (combination[middle].x <= cap):
            left = middle + 1
            index = middle
          else:
            right = middle - 1

        if (index != -1):
          t.y += combination[index].y
        ans = max(ans, t.y)
    return ans


print(Solution().getMaxValue(100, [10, 20, 30, 40, 50], [5, 4, 3, 2, 1]))

# !Vanilla Knapsack TLE
# def getMaxValue(self, s, v, c):
#   # Write your code here
#   nv = len(v)
#   if nv == 0 or s == 0:
#     return 0
#   dp = [[0] * (nv + 1) for _ in range(s + 1)]
#   for ir in range(1, s + 1):
#     for ic in range(1, nv + 1):
#       dp[ir][ic] = dp[ir][ic - 1]
#       if ir >= c[ic - 1]:
#         dp[ir][ic] = max(dp[ir][ic], dp[ir - c[ic - 1]][ic - 1] + v[ic - 1])
#   return dp[s][nv]
