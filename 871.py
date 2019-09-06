class Solution:
  """
  @param a: a positive integer
  @return: the smallest positive integer whose multiplication of each digit equals to a
  """

  def smallestFactorization(self, a):
    # Write your code here
    INT_MAX = int(pow(2, 31)) - 1
    if a == 1:
      return 1
    primes = [2, 3, 5, 7]
    cnt = [0, 0, 0, 0]
    num = ''
    for idx, prime in enumerate(primes):
      while (a % prime == 0):
        cnt[idx] += 1
        a //= prime
    if a > 1:
      return 0
    while (cnt[1] > 1):
      num = '9' + num
      cnt[1] -= 2
    while (cnt[0] > 2):
      num = '8' + num
      cnt[0] -= 3
    while (cnt[3] > 0):
      num = '7' + num
      cnt[3] -= 1
    while (cnt[0] > 0 and cnt[1] > 0):
      num = '6' + num
      cnt[0] -= 1
      cnt[1] -= 1
    while (cnt[2] > 0):
      num = '5' + num
      cnt[2] -= 1
    while (cnt[0] > 1):
      num = '4' + num
      cnt[0] -= 2
    while (cnt[1] > 0):
      num = '3' + num
      cnt[1] -= 1
    while (cnt[0] > 0):
      num = '2' + num
      cnt[0] -= 1
    if len(num) > len(str(INT_MAX)) or int(num) > INT_MAX:
      return 0
    return int(num)
