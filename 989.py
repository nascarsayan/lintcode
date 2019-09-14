class Solution:
  """
  @param nums: an array
  @return: the longest length of set S
  """

  def arrayNesting(self, nums):
    # Write your code here
    size = len(nums)
    visited = [False] * size
    mx = 0
    for i in range(size):
      if visited[i]:
        continue
      visited[i] = True
      j = nums[i]
      curr = 1
      while (not visited[j]):
        visited[j] = True
        j = nums[j]
        curr += 1
      mx = max(mx, curr)
    return mx


print(Solution().arrayNesting([5, 4, 0, 3, 1, 6, 2]))
