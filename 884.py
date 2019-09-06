class Solution:
  """
  @param s: a string
  @return: return a list of integers
  """

  def findPermutation(self, s):
    # write your code here
    size = len(s)
    nums = list(range(1, size + 2))
    nexi = s.find('I')
    if nexi < 0:
      return list(nums[::-1])
    ptr = -1
    per = []
    while (len(nums) > 0):
      st = s.find('I', ptr + 1)
      if st == -1:
        per.extend(nums[::-1])
        break
      chunk = []
      while (ptr < st):
        chunk.append(nums.pop(0))
        ptr += 1
      per.extend(chunk[::-1])
    return per


print(Solution().findPermutation('I'))
