class Solution:
  """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

  def threeSumClosest(self, numbers, target):
    # write your code here
    numbers.sort()
    s = sum(numbers[:3])
    clos = s
    for idx in range(3, len(numbers)):
      st = 0
      fl = idx - 1
      while (st < fl):
        s = numbers[st] + numbers[fl] + numbers[idx]
        if (abs(s - target) < abs(clos - target)):
          clos = s
        if s == target:
          return s
        if s < target:
          st += 1
        else:
          fl -= 1
    return clos


# print(Solution().threeSumClosest([1, 100, 1000, 1000, 0, -100], 1))
