class Solution:
  """
    @param s: a string
    @return: an integer
    """

  def lengthOfLongestSubstring(self, s):
    # write your code here
    l = len(s)
    if l == 0:
      return 0
    winchar = set()
    i = 0
    winchar.add(s[0])
    maxw = 1
    for j, c in enumerate(s[1:]):
      if c in winchar:
        maxw = max(maxw, j - i + 1)
        while c in winchar:
          winchar.remove(s[i])
          i += 1
      winchar.add(c)
    maxw = max(maxw, l - i)
    return maxw


# print(Solution().lengthOfLongestSubstring('abcabcbb'))
# print(Solution().lengthOfLongestSubstring('abcabcde'))
