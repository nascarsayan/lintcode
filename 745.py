class Solution:
  """
  @param L: A positive integer
  @param R: A positive integer
  @return:  the number of interesting subranges of [L,R]
  """

  def PalindromicRanges(self, L, R):
    # test
    def eve(n):
      v = int(str(n) + str(n)[::-1])
      if v > R:
        return
      if L <= v <= R:
        pals.append(v)
        cnt[0] += 1
      for i in range(10):
        eve(n * 10 + i)

    def odd(n):
      v = int(str(n) + str(n)[:-1][::-1])
      if v > R:
        return
      if L <= v <= R:
        pals.append(v)
        cnt[0] += 1
      for i in range(10):
        odd(n * 10 + i)

    cnt = [0]
    pals = []
    if L == 0:
      cnt[0] += 1
      L = 1
    res = 0
    for i in range(1, 10):
      eve(i)
      odd(i)
    pals = [L - 1] + list(sorted(pals)) + [R + 1]
    invs = list(map(lambda x: x[1] - x[0], zip(pals, pals[1:])))
    size = len(invs)
    res = 0
    if size == 1:
      return ((invs[0]) * (invs[0] - 1)) // 2
    for i in range(size - 1):
      for j in range(i + 2, size, 2):
        res += invs[i] * invs[j]
    for i in range(size):
      res += ((invs[i]) * (invs[i] - 1)) // 2
    return res


print(Solution().PalindromicRanges(11, 22))
