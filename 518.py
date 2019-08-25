import heapq


class Solution:
  """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """

  def nthSuperUglyNumber(self, n, primes):
    # write your code here
    if n == 1:
      return 1
    primes = sorted(primes)
    hp = primes[:]
    nth = None
    for i in range(1, n):
      nth = heapq.heappop(hp)
      for fac in primes:
        if nth * fac not in hp:
          heapq.heappush(hp, nth * fac)
    return nth
