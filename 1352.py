class Solution:
  """
  @param version1: the first given number
  @param version2: the second given number
  @return: the result of comparing
  """

  def compareVersion(self, version1, version2):
    # Write your code here
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    l1, l2 = len(v1), len(v2)
    for i in range(min(l1, l2)):
      if v1[i] > v2[i]:
        return 1
      if v1[i] < v2[i]:
        return -1
    if l1 == l2:
      return 0
    return (l1 - l2) // abs(l1 - l2)


print(Solution().compareVersion('1.01.1', '1.1.1'))
