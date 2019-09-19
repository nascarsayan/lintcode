from collections import Counter, deque


class Solution:
  """
  @param nums: a continuous stream of numbers
  @param number: a number
  @return: returns the first unique number
  """

  def firstUniqueNumber(self, nums, number):
    # Write your code here
    que = deque()
    cnt = Counter()
    for num in nums:
      cnt[num] += 1
      if cnt[num] == 1:
        que.append(num)
      if num == number:
        while (que and cnt[que[0]] > 1):
          que.popleft()
        if que:
          return que[0]
        return -1
    return -1
