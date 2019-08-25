class Solution:
  """
  @param nums: an array
  @param k: an integer
  @return: the number of subarrays where the product of all the elements in the subarray is less than k
  """

  def numSubarrayProductLessThanK(self, nums, k):
    # Write your code here
    size = len(nums)
    if size == 0 or k < 2:
      return 0
    prod = 1
    tot = 0
    st = 0
    for fl in range(size):
      prod *= nums[fl]
      while (st <= fl and prod >= k):
        prod //= nums[st]
        st += 1
      tot += fl - st + 1
    return tot
