class Solution:
  """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

  def backPack(self, m, A):
    # write your code here
    values = {0}
    for a in A:
      newv = set()
      for v in values:
        if v + a == m:
          return m
        if v + a < m:
          newv.add(v + a)
      values.update(newv)
    return max(values)
