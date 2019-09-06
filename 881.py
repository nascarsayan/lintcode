from collections import Counter


class Solution:
  """
  @param picture: a 2D char array
  @param N: an integer
  @return: return a integer
  """

  def findBlackPixel(self, picture, N):
    # write your code here
    nr = len(picture)
    if nr == 0:
      return 0
    nc = len(picture[0])
    if nc == 0:
      return 0
    bcnt = [0] * nc
    for ir in range(nr):
      for ic in range(nc):
        bcnt[ic] += (0, 1)[picture[ir][ic] == 'B']
    idcs = set()
    for ic in range(nc):
      if bcnt[ic] == N:
        idcs.add(ic)
    sarr = [''.join(row) for row in picture]
    cnt = Counter()
    for es in sarr:
      cnt[es] += 1
    tot = 0
    for k, v in cnt.most_common():
      if v != N:
        continue
      for idx in idcs:
        if k[idx] == 'B':
          tot += N
    return tot


print(Solution().findBlackPixel(["WBWBBW", "WBWBBW", "WBWBBW", "WWBWBW"], 3))
