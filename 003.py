# https://www.lintcode.com/problem/digit-counts/
class Solution:
  """
  @param k: An integer
  @param n: An integer
  @return: An integer denote the count of digit k in 1..n
  """
  def digitCounts(self, k, n):
    # write your code here
    DIV = 10
    curr = 1
    total = 0
    if k == 0:
      total = 1
      while (curr * 10 <= n):
        total += (n // (curr * 10) - 1) * curr
        dig = (n % (curr * 10)) // curr
        if (dig > k):
          total += curr
        elif (dig == k):
          total += (n % curr) + 1
        curr *= DIV
    else:
      while (curr <= n):
        total += (n // (curr * 10)) * curr
        dig = (n % (curr * 10)) // curr
        if (dig > k):
          total += curr
        elif (dig == k):
          total += (n % curr) + 1
        curr *= DIV
    return total

print(Solution().digitCounts(0, 21))