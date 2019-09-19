# import bisect


class Solution:
  """
  @param S: A list of integers
  @return: An integer
  """

  def triangleCount(self, S):
    # write your code here
    S.sort()
    size = len(S)
    tot = 0
    for k in range(2, size)[::-1]:
      i, j = 0, k - 1
      while (i < j):
        if S[i] + S[j] > S[k]:
          tot += j - i
          j -= 1
        else:
          i += 1
    return tot


# !O(n^2 lgn)

# def triangleCount(self, S):
#   # write your code here
#   S.sort()
#   size = len(S)
#   tot = 0
#   for i in range(size - 2):
#     for j in range(i + 1, size - 1):
#       k = bisect.bisect_right(S, S[i] + S[j] - 1) - 1
#       if k > j and k < size:
#         tot += k - j
#   return tot

print(Solution().triangleCount([4, 4, 4, 4]))
