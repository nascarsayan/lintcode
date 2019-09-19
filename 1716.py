class Solution:
  """
  @param S: a string
  @return: the minimum number
  """

  def minFlipsMonoIncr(self, S):
    # Write your code here.
    size = len(S)
    if size == 0:
      return 0
    mp = {'0': 0, '1': 1}
    mpr = {'0': 1, '1': 0}
    n0, n1 = list(map(lambda x: mpr[x], S)), list(map(lambda x: mp[x], S))
    for i in range(1, size):
      n1[i] += n1[i - 1]
    for i in range(size - 1)[::-1]:
      n0[i] += n0[i + 1]
    mn = min(n1[-1], n0[0])
    for i in range(1, size):
      mn = min(mn, n1[i - 1] + n0[i])
    return mn
