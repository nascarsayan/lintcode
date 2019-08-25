class Solution(object):

  def orderOfLargestPlusSign(self, N, mines):
    """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
    # Methods to reduce computational time:
    # 1. convert mines from list to dictionary. O(n^3) to O(n^2)
    # 2. use try/except instead of if else to deal with matrix boundary

    L = [
        [0 for x in range(N)] for y in range(N)
    ]  #L[i][j]: number of continuous 1 from L[i][j] towards its left, L[i][j] included.
    R = [[0 for x in range(N)] for y in range(N)]  #Right
    U = [[0 for x in range(N)] for y in range(N)]  #Up
    D = [[0 for x in range(N)] for y in range(N)]  #Down

    dicMines = {(mine[0], mine[1]) for mine in mines
               }  # convert mines from list to dictionary

    # calcuate L and D in O(n^2) time
    for i in range(N):
      for j in range(N):
        if (i, j) not in dicMines:
          # use try/except instead of if/else to reduce time, if/else method is presented below as well
          try:
            L[i][j] = L[i][j - 1] + 1
          except Exception:
            L[i][j] = 1
          try:
            D[i][j] = D[i - 1][j] + 1
          except Exception:
            D[i][j] = 1

          #if/else method presented for reference
          #L[i][j] = L[i][j-1] + 1 if j > 0 else 1
          #D[i][j] = D[i-1][j] + 1 if i > 0 else 1

    # calcuate R and U in O(n^2) time
    for i in range(N - 1, -1, -1):
      for j in range(N - 1, -1, -1):
        if (i, j) not in dicMines:
          try:
            R[i][j] = R[i][j + 1] + 1
          except Exception:
            R[i][j] = 1
          try:
            U[i][j] = U[i + 1][j] + 1
          except Exception:
            U[i][j] = 1

          #R[i][j] = R[i][j+1] + 1 if j < N-1 else 1
          #U[i][j] = U[i+1][j] + 1 if i < N-1 else 1
    MaxK = 0
    MaxK = max(
        min(L[i][j], R[i][j], U[i][j], D[i][j])
        for i in range(N)
        for j in range(N))
    return (MaxK)


print(Solution().orderOfLargestPlusSign(1000, []))
