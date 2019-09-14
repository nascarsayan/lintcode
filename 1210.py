# from collections import defaultdict


class Solution:
  """
  @param nums: an integer array
  @return: all the different possible increasing subsequences of the given array
  """

  def findSubsequences(self, nums):
    # Write your code here
    def recurse(idx, path):
      psize = len(path)
      if idx == size:
        if psize > 1:
          incs.add(tuple(path))
        return
      if nums[idx] >= path[-1]:
        # j = psize - 1
        # while (j >= 0 and path[j] == nums[idx]):
        #   j -= 1
        # pcnt = psize - j
        # if pcnt == fre[idx]:
        recurse(idx + 1, path + [nums[idx]])
      recurse(idx + 1, path)

    # cnt = defaultdict(int)
    size = len(nums)
    # fre = []
    # for i, num in enumerate(nums):
    #   cnt[num] += 1
    #   fre.append(cnt[num])
    incs = set()
    for i in range(size - 1):
      st = [nums[i]]
      recurse(i + 1, st)
    return list(map(list, incs))


print(Solution().findSubsequences([4, 6, 7, 7]))
