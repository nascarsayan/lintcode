class Solution:
  """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

  def sortColors(self, nums):
    # write your code here
    size = len(nums)
    if size < 2:
      return
    st = -1
    fl = size
    idx = 0
    while (idx < fl):
      if nums[idx] == 0:
        st += 1
        nums[idx], nums[st] = nums[st], nums[idx]
        if st == idx:
          idx += 1
      elif nums[idx] == 2:
        fl -= 1
        nums[idx], nums[fl] = nums[fl], nums[idx]
      else:
        idx += 1
