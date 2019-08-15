from collections import defaultdict


class Solution:
  """
    @param N: int
    @param K: int
    @param r: int
    @param c: int
    @return: the probability
    """

  def knightProbability(self, N, K, r, c):
    # Write your code here.
    w1 = defaultdict(int)
    w2 = defaultdict(int)
    if not (0 <= r < N and 0 <= c < N):
      return 0
    for ir in range(N):
      for ic in range(N):
        w1[(ir, ic)] = sum([
            1 for (tr,
                   tc) in [(-1,
                            -2), (-2,
                                  -1), (-2,
                                        1), (-1,
                                             2), (1, 2), (2, 1), (2, -1), (1,
                                                                           -2)]
            if 0 <= ir + tr < N and 0 <= ic + tc < N
        ])/8
    for ik in range(1, K):
      for ir in range(N):
        for ic in range(N):
          w2[(ir, ic)] = sum([
              w1[(ir + tr, ic + tc)]
              for (tr,
                   tc) in [(-1,
                            -2), (-2,
                                  -1), (-2,
                                        1), (-1,
                                             2), (1, 2), (2, 1), (2, -1), (1,
                                                                           -2)]
              if 0 <= ir + tr < N and 0 <= ic + tc < N
          ])/8
      w1, w2 = w2, w1
    return w1[(r, c)]


print(Solution().knightProbability(20, 83, 7, 13))
