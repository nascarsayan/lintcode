class Solution:
  """
    @param num: a non-negative integer
    @return: english words representation
    """

  def numberToWords(self, num):
    # Write your code here
    kmark = ['', 'Thousand', 'Million', 'Billion']
    dmark = [
        '', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
        'Eighty', 'Ninety'
    ]
    umark = [
        '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
        'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
    ]
    if num == 0:
      return 'Zero'
    kcurr = 0
    wd = []
    while (num > 0):
      uval = num % 100
      kwd = []
      if uval < 20:
        kwd = [umark[uval]] + kwd
      else:
        kwd = [dmark[uval // 10]] + [umark[uval % 10]] + kwd
      dval = (num // 100) % 10
      if dval > 0:
        kwd = [umark[dval]] + ['Hundred'] + kwd
      kwd += [kmark[kcurr]]
      kcurr += 1
      wd = kwd + wd
      num = num // 1000
    return ' '.join(list(filter(lambda x: len(x) > 0, wd)))


print(Solution().numberToWords(1234567))
