class Solution:
  """
  @param nums: a list of n integers
  @return: true if there is a 132 pattern or false
  """

  def find132pattern(self, nums):
    # write your code here
    stac = []
    uphill = False
    mnp = float('inf')
    for num in nums:
      if len(stac) == 0 or stac[-1] > num:
        stac.append(num)
        if uphill and len(stac) > 1 and mnp < stac[1]:
          return True
      else:
        while (len(stac) > 0 and stac[-1] <= num):
          mnp = min(mnp, stac.pop(-1))
        stac.append(num)
        uphill = True
    return False
