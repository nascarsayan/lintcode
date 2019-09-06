class Solution:
  """
  @param nums: an array of Integer
  @param target: target = nums[index1] + nums[index2]
  @return: [index1 + 1, index2 + 1] (index1 < index2)
  """

  def twoSum(self, nums, target):
    # write your code here
    st, fl = 0, len(nums) - 1
    while (st < fl):
      tot = nums[st] + nums[fl]
      if tot == target:
        return [st + 1, fl + 1]
      if tot > target:
        fl -= 1
      else:
        st += 1
    return [None, None]
