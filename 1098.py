class Solution:
  """
  @param nums: the list
  @return: the sum of all paths from the root towards the leaves
  """

  def pathSumIV(self, nums):
    # Write your code here.
    nodes = [-1] * 16
    for num in nums:
      d1, d2, d3 = list(map(int, str(num)))
      nodes[2**(d1 - 1) + d2 - 1] = d3
    res = 0

    for i in range(2, 16):
      if nodes[i] != -1:
        nodes[i] += nodes[i // 2]
        if i * 2 > 15 or (nodes[i * 2] == nodes[i * 2 + 1] == -1):
          res += nodes[i]
    return res


print(Solution().pathSumIV([]))
