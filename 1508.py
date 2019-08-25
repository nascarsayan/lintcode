class Solution:
  """
    @param A: a matrix
    @return: the score
    """

  def matrixScore(self, A):
    # Write your code here.
    nr = len(A)
    if nr == 0:
      return 0
    nc = len(A[0])
    if nc == 0:
      return 0
    while (True):
      mxr, inc = None, 0
      for ir in range(nr):
        tinc = int(''.join([str(k ^ 1) for k in A[ir]]), 2) - int(
            ''.join([str(k) for k in A[ir]]), 2)
        if tinc > inc:
          inc, mxr = tinc, ir
      mxc = None
      for ic in range(nc):
        tinc = (nc - 2 * sum(r[ic] for r in A)) << (nc - 1 - ic)
        if tinc > inc:
          inc, mxc, mxr = tinc, ic, None
      print(inc)
      if mxr is not None:
        for ic in range(nc):
          A[mxr][ic] = A[mxr][ic] ^ 1
      elif mxc is not None:
        for ir in range(nr):
          A[ir][mxc] = A[ir][mxc] ^ 1
      else:
        break
    return sum(
        list(
            map(lambda x: int(x, 2),
                [''.join([str(k) for k in row]) for row in A])))


print(Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
