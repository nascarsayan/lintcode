import heapq


class Solution:
  """
    @param numbers: the numbers
    @return: the minimum cost
    """

  def mergeNumber(self, numbers):
    # Write your code here
    cost = 0
    heapq.heapify(numbers)
    while (len(numbers) > 1):
      nwn = heapq.heappop(numbers) + heapq.heappop(numbers)
      cost += nwn
      heapq.heappush(numbers, nwn)
    return cost


print(Solution().mergeNumber([1, 2, 3, 4]))
