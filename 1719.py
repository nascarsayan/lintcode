class Solution:
  """
    @param A: the given integer array
    @param target: the given integer target
    @return: the number of tuples
    """

  def threeSumMulti(self, A, target):
    # Write your code here
    mx = max(A)
    occ = [0] * (mx + 1)
    for i, a in enumerate(A):
      occ[a] += 1
    tot = 0
    if target > 3 * mx:
      return 0
    if target % 3 == 0 and occ[target // 3] >= 3:
      sz = occ[target // 3]
      tot += (sz * (sz - 1) * (sz - 2)) // 6
    for i in range(mx + 1):
      rem = target - (2 * i)
      if rem > mx or rem == i:
        continue
      if rem < 0:
        break
      if occ[i] >= 2 and occ[rem] >= 1:
        sz = occ[i]
        tot += ((sz * (sz - 1)) // 2) * occ[rem]

    for i in range(min(mx + 1, (target + 2) // 3)):
      for j in range(i + 1, min(mx + 1, (target - i + 2) // 2)):
        rem = target - (i + j)
        if rem > mx:
          continue
        if rem <= j:
          break
        tot += occ[i] * occ[j] * occ[rem]
    return tot % (10**9 + 7)


print(Solution().threeSumMulti([0, 0, 0], 0))
