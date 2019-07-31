from collections import defaultdict
import json


class Solution:
  """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

  def fourSum(self, numbers, target):
    # write your code here
    numbers.sort()
    sum2pair = defaultdict(list)
    size = len(numbers)
    combi = set()
    if size < 4:
      return []
    for i1 in range(size - 1):
      for i2 in range(i1 + 1, size):
        sum2pair[numbers[i1] + numbers[i2]].append([i1, i2])
    for s1 in sum2pair.keys():
      s2 = target - s1
      if s2 in sum2pair:
        a1 = sum2pair[s1]
        a2 = sum2pair[s2]
        for p1 in a1:
          for p2 in list(filter(lambda x: x[0] > p1[0], a2)):
            idxs = sorted(list(set(p1 + p2)))
            if len(idxs) == 4:
              combi.add(json.dumps(list(map(lambda i: numbers[i], idxs))))
    return [json.loads(q) for q in combi]


# print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
# Counter TLE
