class Solution:
  """
  @param n: an integer
  @return: 1 - n in lexicographical order
  """

  def lexicalOrder(self, n):
    # write your code here
    def recurse(m):
      if m > n:
        return
      res.append(m)
      for i in range(10):
        recurse(m * 10 + i)

    res = []
    for i in range(1, 10):
      recurse(i)
    return res


print(Solution().lexicalOrder(200))
