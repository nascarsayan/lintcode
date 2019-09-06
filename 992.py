class Solution:
  """
  @param n: the number of integers
  @param k: the number of distinct integers
  @return: any of answers meet the requirment
  """

  def constructArray(self, n, k):
    # Write your code here
    cons = [1]
    dif = n - 1
    while (k > 1):
      cons.append(cons[-1] + dif)
      dif = -((abs(dif) - 1) * (dif // abs(dif)))
      k -= 1
    dif = dif // abs(dif)
    for _ in range(len(cons), n):
      cons.append(cons[-1] + dif)
    return cons


print(Solution().constructArray(2, 1))
