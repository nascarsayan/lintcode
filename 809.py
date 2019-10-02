class Solution:
  """
  @param N: the row
  @param K: the index
  @return:  the K-th indexed symbol in row N
  """

  def kthGrammar(self, N, K):
    # Write your code here
    if N == 1:
      return 0
    for n in range(3, N + 1)[::-1]:
      tot = (1 << (n - 1))
      if K > (tot >> 1):
        K = ((K - 1 - (tot >> 1) + (tot >> 2)) % (tot >> 1)) + 1
    return (K + 1) % 2


print(Solution().kthGrammar(4, 5))
