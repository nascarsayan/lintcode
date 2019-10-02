class Solution:
  """
  @param num: a string
  @return: Is it a valid additive number
  """

  def isAdditiveNumber(self, num):
    # Write your code here
    def recurse(n1, n2, ptr):
      if ptr == size:
        return True
      n3 = str(int(n1) + int(n2))
      if num[ptr:].startswith(n3):
        return recurse(n2, n3, ptr + len(n3))
      return False

    size = len(num)
    if size < 3:
      return False
    for i in range(size - 2):
      for j in range(i + 1, size - 1):
        if size - j - 1 < max(i + 1, j - i):
          continue
        n1 = num[:i + 1]
        n2 = num[i + 1:j + 1]
        if all(x[0] != 0 or len(x) == 1 for x in [n1, n2]):
          if recurse(n1, n2, j + 1):
            return True
    return False


print(Solution().isAdditiveNumber("123"))
