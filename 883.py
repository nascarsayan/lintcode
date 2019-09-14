class Solution:
  """
  @param nums: a list of integer
  @return: return a integer, denote  the maximum number of consecutive 1s
  """

  def findMaxConsecutiveOnes(self, nums):
    # write your code here
    mxc = 0
    st, mid, fl, size = 0, None, 0, len(nums)
    while (st < size and fl < size):
      if nums[fl] == 0:
        if mid is not None:
          mxc = max(mxc, fl - st)
          st = mid + 1
        mid = fl
      fl += 1

    mxc = max(mxc, fl - st)
    return mxc


print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1, 1, 0, 1]))
