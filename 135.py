import bisect


class Solution:

  def recurse(self, candidates, ncan, rem, idx, currcom, allcom):
    if idx >= ncan or candidates[idx] > rem:
      return
    rem -= candidates[idx]
    if rem == 0:
      allcom.append(currcom + [candidates[idx]])
    else:
      for nex in range(idx, ncan):
        if rem < candidates[nex]:
          break
        self.recurse(candidates, ncan, rem, nex, currcom + [candidates[idx]],
                     allcom)

  """
  @param candidates: A list of integers
  @param target: An integer
  @return: A list of lists of integers
  """

  def combinationSum(self, candidates, target):
    # write your code here
    candidates = sorted(list(set(candidates)))
    rt = bisect.bisect_right(candidates, target)
    candidates = candidates[:rt]
    allcom = []
    size = len(candidates)
    for start in range(size):
      self.recurse(candidates, size, target, start, [], allcom)
    return allcom


# print(Solution().combinationSum([2, 3, 5, 7], 7))

# def combinationSum(self, candidates, target):
#   # write your code here
#   size = len(candidates)
#   if size == 0:
#     return []
#   candidates.sort()
#   st = 0
#   fl = 0
#   total = candidates[0]
#   combi = []
#   while (st <= fl and fl < size):
#     if total == target:
#       combi.append(candidates[st:fl + 1])
#       fl += 1
#       if (fl < size):
#         total += candidates[fl]
#     while (total < target and fl < size):
#       fl += 1
#       if (fl < size):
#         total += candidates[fl]
#     if (fl == size):
#       break
#     while (total > target and st <= fl):
#       total -= candidates[st]
#       st += 1
#   return combi
