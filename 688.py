class Solution:
  """
  @param num: the number
  @return: the number in words
  """

  def convertWords(self, num):
    # Write your code here
    kmark = ['', 'thousand', 'million', 'billion']
    dmark = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety'
    ]
    umark = [
        '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    if num == 0:
      return 'zero'
    kcurr = 0
    wd = []
    while (num > 0):
      uval = num % 100
      if uval > 0:
        kwd = []
        if uval < 20:
          kwd = [umark[uval]] + kwd
        else:
          kwd = [dmark[uval // 10]] + [umark[uval % 10]] + kwd
        dval = (num // 100) % 10
        if dval > 0:
          kwd = [umark[dval]] + ['hundred'] + kwd
        kwd += [kmark[kcurr]]
        wd = kwd + wd
      kcurr += 1
      num = num // 1000
    return ' '.join(list(filter(lambda x: len(x) > 0, wd)))


print(Solution().convertWords(2000000000))
