from collections import Counter
from functools import cmp_to_key


class Solution:
  """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

  def topKFrequentWords(self, words, k):
    # write your code here
    def mycmp(x, y):
      if x[1] == y[1]:
        if x[0] < y[0]:
          return -1
        return 1
      return y[1] - x[1]

    cnt = Counter(words)
    cnt2 = [(ke, cnt[ke]) for ke in cnt]
    cnt2.sort(key=cmp_to_key(mycmp))
    return [p[0] for p in cnt2[:k]]


print(Solution().topKFrequentWords([
    "yes", "lint", "code", "yes", "code", "baby", "you", "baby", "chrome",
    "safari", "lint", "code", "body", "lint", "code"
], 3))
