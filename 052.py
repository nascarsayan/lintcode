class Solution:
  """
    @param nums: A list of integers
    @return: A list of integers
    """

  def nextPermutation(self, nums):
    # write your code here
    size = len(nums)
    if size < 2:
      return nums
    idx = size - 1
    while (idx > 0):
      if nums[idx - 1] < nums[idx]:
        if idx == size - 1:
          nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]
        else:
          mingtidx = idx
          for ridx in range(idx + 1, size):
            if nums[ridx] < nums[mingtidx] and nums[ridx] > nums[idx - 1]:
              mingtidx = ridx
          nums[idx - 1], nums[mingtidx] = nums[mingtidx], nums[idx - 1]
          nums = nums[:idx] + sorted(nums[idx:])
        break
      idx -= 1
    if idx == 0:
      nums.sort()
    return nums


# print(Solution().nextPermutation([1, 3, 3, 2]))

# Failed attempt
# def nextPermutation(self, nums):
#   # write your code here
#   size = len(nums)
#   if size < 2:
#     return nums
#   snums = sorted(nums)
#   sortedpos = defaultdict(list)
#   for k, v in enumerate(snums):
#     sortedpos[v].append(k)
#   # sortedpos = dict([(v, k) for k, v in enumerate(snums)])
#   seq = [sortedpos[num].pop() for num in nums]
#   print(seq)
#   enc = []
#   idx = size - 1
#   while (idx > 0):
#     enc.append(seq[idx])
#     if seq[idx - 1] < seq[idx]:
#       if len(enc) == 0:
#         seq[idx - 1], seq[idx] = seq[idx], seq[idx - 1]
#       else:
#         mingtidx = 0
#         for idx in range(1, len(enc)):
#           if enc[idx] < enc[mingtidx] and enc[idx] > seq[idx - 1]:
#             mingtidx = idx
#         seq[idx - 1], enc[mingtidx] = enc[mingtidx], seq[idx - 1]
#         seq = seq[:idx] + sorted(enc)
#       break
#     idx -= 1
#   if idx == 0:
#     seq.sort()
#   print(seq)
#   return list(map(lambda x: snums[x], seq))