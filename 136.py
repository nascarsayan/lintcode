# import json


class Solution:

  def recurse(self, s, curr, coln):
    size = len(s)
    if size == 0:
      coln.append(curr)
      return
    for i in range(size):
      subs = s[:i + 1]
      if subs == ''.join(reversed(subs)):
        self.recurse(s[i + 1:], curr + [subs], coln)

  """
  @param: s: A string
  @return: A list of lists of string
  """

  def partition(self, s):
    # write your code here
    coln = []
    self.recurse(s, [], coln)
    return coln


# print(Solution().partition('seeslaveidemonstrateyetartsnomedievalsees'))

# TLE

# class Solution:

#   def recurse(self, curr, coln):
#     coln.add(json.dumps(curr))
#     size = len(curr)
#     for idx in range(1, size - 1):
#       if ''.join(reversed(curr[idx - 1])) == curr[idx + 1]:
#         newpal = curr[idx - 1] + curr[idx] + curr[idx + 1]
#         self.recurse(curr[:idx - 1] + [newpal] + curr[idx + 2:], coln)
#     for idx in range(size - 1):
#       if ''.join(reversed(curr[idx])) == curr[idx + 1]:
#         newpal = curr[idx] + curr[idx + 1]
#         self.recurse(curr[:idx] + [newpal] + curr[idx + 2:], coln)

#   """
#   @param: s: A string
#   @return: A list of lists of string
#   """

#   def partition(self, s):
#     # write your code here
#     coln = set()
#     self.recurse(list(s), coln)
#     return [json.loads(s) for s in coln]
