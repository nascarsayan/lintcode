class Solution:
  """
  @param n:
  @param nums:
  @return: return the sum of maximum OR sum, minimum OR sum, maximum AND sum, minimum AND sum.
  """

  def getSum(self, n, nums):
    # write your code here
    inf, ninf = float('inf'), float('-inf')
    mxa, mna, mxo, mno = ninf, nums[0], nums[0], inf
    for num in nums:
      mxa = max(mxa, num)
      mna &= num
      mxo |= num
      mno = min(mno, num)
    return mxa + mna + mxo + mno
