from collections import defaultdict


class Solution:
  """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

  def multiply(self, A, B):
    # write your code here
    rowa = defaultdict(list)
    rowb = defaultdict(list)
    cola = defaultdict(list)
    colb = defaultdict(list)
    try:
      nra, nrb, nca, ncb = len(A), len(B), len(A[0]), len(B[0])
    except IndexError:
      return []
    ab = [[0] * ncb for _ in range(nra)]
    for ira in range(nra):
      for ica in range(nca):
        if A[ira][ica] != 0:
          rowa[ira].append(ica)
          cola[ica].append(ira)
    for irb in range(nrb):
      for icb in range(ncb):
        if B[irb][icb] != 0:
          rowb[irb].append(icb)
          colb[icb].append(irb)
    for ira in range(nra):
      for icb in range(ncb):
        v1 = rowa[ira]
        v2 = colb[icb]
        p1, p2 = 0, 0
        while (p1 < len(v1) and p2 < len(v2)):
          if v1[p1] == v2[p2]:
            ab[ira][icb] += A[ira][v1[p1]] * B[v2[p2]][icb]
            p1 += 1
            p2 += 1
          elif v1[p1] < v2[p2]:
            p1 += 1
          else:
            p2 += 1
    return ab


print(Solution().multiply([[1, 0, 0], [-1, 0, 3]],
                          [[7, 0, 0], [0, 0, 0], [0, 0, 1]]))
