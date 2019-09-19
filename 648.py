from collections import defaultdict


class ValidWordAbbr:
  """
    @param: dictionary: a list of words
    """

  def __init__(self, dictionary):
    # do intialization if necessary
    self.abv = defaultdict(set)
    for wd in dictionary:
      sz = len(wd)
      if sz < 3:
        self.abv[(wd, sz)].add(wd)
      else:
        self.abv[(wd[0] + wd[-1], sz)].add(wd)
    # self.nuniq = [k for k in self.abv if len(self.abv[k]) > 1]

  """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """

  def isUnique(self, word):
    # write your code here
    sz = len(word)
    tup = (word, sz)
    if sz >= 3:
      tup = (word[0] + word[-1], sz)
    return (tup not in self.abv or
            len(self.abv[tup]) == 1 and word in self.abv[tup])


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)
