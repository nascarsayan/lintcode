from collections import Counter


class Solution:
  """
  @param licensePlate: a string
  @param words: List[str]
  @return: return a string
  """

  def shortestCompletingWord(self, licensePlate, words):
    # write your code here
    def getcnt(word):
      return Counter(list(filter(lambda x: 97 <= ord(x) <= 122, word.lower())))

    lens = sorted(list((len(wd), i) for i, wd in enumerate(words)))
    lpc = getcnt(licensePlate)
    for _, idx in lens:
      word = words[idx]
      wdc = getcnt(word)
      if all(wdc[k] >= lpc[k] for k in lpc.keys()):
        return word
    return None


print(Solution().shortestCompletingWord("1s3 456",
                                        ["looks", "pest", "stew", "show"]))
