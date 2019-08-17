class Solution:
  """
    @param nums: a list of integers
    @return: return a boolean
    """

  def xorGame(self, nums):
    # write your code here
    x = set()
    for num in nums:
      if num not in x:
        x.add(num)
      else:
        x.remove(num)
    if len(x) == 1:
      return x.pop() == 0
    return len(x) % 2 == 0
