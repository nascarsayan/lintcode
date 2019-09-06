class Solution:
  """
  @param n: a integer
  @return: return a 2D array
  """

  def getFactors(self, n):
    # write your code here
    def sieve(n):
      primes = []
      nums = [True] * (n + 1)
      nums[0], nums[1] = False, False
      sq = int(pow(n, 0.5)) + 1
      for i in range(2, sq + 1):
        if nums[i]:
          j = i * 2
          while (j <= n):
            nums[j] = False
            j += i
      for i in range(2, n + 1):
        if nums[i]:
          primes.append(i)
      return primes

    if n == 1:
      return [[1]]
    primes = sieve(n)
    # for pr in primes:
    #   if


print(Solution().getFactors(100))
