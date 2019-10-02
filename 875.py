from copy import deepcopy


class Solution:
  """
  @param M: the 01 matrix
  @return: the longest line of consecutive one in the matrix
  """

  def longestLine(self, M):
    # Write your code here
    try:
      nr, nc = len(M), len(M[0])
    except IndexError:
      return 0
    N, W, NW, NE = deepcopy(M), deepcopy(M), deepcopy(M), deepcopy(M)
    mx = 0
    for ir in range(nr):
      for ic in range(nc):
        if M[ir][ic] == 0:
          continue
        if ir > 0:
          N[ir][ic] += N[ir - 1][ic]
        if ic > 0:
          W[ir][ic] += W[ir][ic - 1]
        if ir > 0 and ic > 0:
          NW[ir][ic] += NW[ir - 1][ic - 1]
        if ir > 0 and ic < nc - 1:
          NE[ir][ic] += NE[ir - 1][ic + 1]
        mx = max(mx, N[ir][ic], W[ir][ic], NW[ir][ic], NE[ir][ic])
    return mx
