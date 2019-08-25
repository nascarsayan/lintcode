class Solution:
  """
  @param n: the length of strobogrammatic number
  @return: All strobogrammatic numbers
  """

  def findStrobogrammatic(self, n):
    # write your code here
    s1 = ['0', '1', '8']
    s2 = [('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
    nums = ['']
    if n < 1:
      return nums
    if n == 1:
      return s1
    if (n % 2 == 1):
      nums = s1[:]
    for i in range(n // 2):
      t = []
      for num in nums:
        for s2e in s2:
          t.append(s2e[0] + num + s2e[1])
        if i < n // 2 - 1:
          t.append('0' + num + '0')
      nums = t
    return nums


# print(Solution().findStrobogrammatic(5))
