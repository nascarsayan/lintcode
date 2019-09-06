class Solution:
  """
  @param words: a string array
  @return: the maximum product
  """

  def maxProduct(self, words):
    # Write your code here
    mx = 0
    sets = []
    lns = []
    for word in words:
      sets.append(set(word))
      lns.append(len(word))
    size = len(sets)
    for i in range(size - 1):
      for j in range(i + 1, size):
        if len(sets[i].intersection(sets[j])) == 0:
          mx = max(mx, lns[i] * lns[j])
    return mx


print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
