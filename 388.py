from itertools import permutations


class Solution:
  """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """

  def getPermutation(self, n, k):
    # write your code here
    perm = list(permutations(range(1, n + 1)))
    size = len(perm)
    return ''.join([str(x) for x in perm[(k - 1) % size]])


# print(Solution().getPermutation(3, 4))
