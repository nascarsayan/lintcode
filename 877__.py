class Solution:
  """
  @param nums: a list of integer
  @return: return a boolean
  """

  def splitArray(self, nums):
    # write your code here
    size = len(nums)
    if size < 7:
      return False
    tot = [0]
    for num in nums:
      tot.append(tot[-1] + num)
    tot.pop(0)
    for i in range(3, size - 3):
      if tot[i - 1] % 2 == 1:
        continue
      if tot[-1] - tot[i] == tot[i - 1]:
        fl = False
        for j in range(1, i - 1):
          if tot[j - 1] == tot[i - 1] - tot[j]:
            fl = True
            break
