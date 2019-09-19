class Solution:
  """
  @param nums: an array of integer
  @return: the first missing prime number
  """

  def firstMissingPrime(self, nums):
    # write your code here
    nums.sort()
    size = len(nums)
    if size == 0 or nums[0] != 2:
      return 2
    nex = 0
    fl = nums[-1] * 2
    sieve = [True] * (fl + 1)
    sieve[0] = sieve[1] = False
    for st in range(2, fl + 1):
      if not sieve[st]:
        continue
      if nex >= size or nums[nex] != st:
        return st
      nex += 1
      mid = 2 * st
      while (mid <= fl):
        sieve[mid] = False
        mid += st
    return None


print(Solution().firstMissingPrime([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]))
