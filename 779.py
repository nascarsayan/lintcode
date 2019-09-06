class Solution:
  """
  @param word: the given word
  @return: the generalized abbreviations of a word
  """

  def generateAbbreviations(self, word):
    # Write your code here
    size = len(word)
    res = []
    for i in range(2**size):
      mask = '{num:0{width}b}'.format(num=i, width=size)[::-1]
      abv = []
      for j, c in enumerate(mask):
        if c == '0':
          abv.append(word[j])
        else:
          if abv and type(abv[-1]) is int:
            abv[-1] += 1
          else:
            abv.append(1)
      res.append(''.join(list(map(str, abv))))
    return res


print(Solution().generateAbbreviations('word'))
