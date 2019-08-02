class Solution:
  """
  @param nums: an array of positive and negative integers
  @return: if there is a loop in this array
  """

  def circularArrayLoop(self, nums):
    # Write your code here
    size = len(nums)
    if size < 2:
      return False
    visited = [False] * size
    for idx in range(size):
      if nums[idx] % size == 0:
        visited[idx] = True
    for st in range(size):
      curr = st
      chain = set([curr])
      sgn = (1, -1)[nums[curr] < 0]
      while (not visited[curr]):
        visited[curr] = True
        if sgn * nums[curr] < 0:
          visited[curr] = False
          break
        curr = (curr + nums[curr]) % size
        if curr in chain:
          return True
        chain.add(curr)
    return False
