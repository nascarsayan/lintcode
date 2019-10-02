import itertools


class Solution:
  """
    @param n: An integer
    @return: An array storing 1 to the largest number with n digits.
    """

  def numbersByRecursion(self, n):
    # write your code here
    res = list(range(10))
    if n == 0:
      return []

    def recurse(m):
      if m == n:
        return
      st = 10**(m - 1)
      res.extend(
          list(
              itertools.chain.from_iterable(
                  list(
                      map(lambda x: list(map(lambda y: 10 * x + y, range(10))),
                          res[st:])))))
      recurse(m + 1)

    recurse(1)
    return res[1:]


print(Solution().numbersByRecursion(2))
