class Solution:
  """
  @param s: the given string
  @param numRows: the number of rows
  @return: the string read line by line
  """

  def convert(self, s, numRows):
    # Write your code here
    def get(s, i):
      if len(s) > i:
        return s[i]
      return ''

    size = len(s)
    if numRows == 0 or size == 0:
      return ''
    if numRows == 1:
      return s
    chainlen = 2 * numRows - 2
    turns = size // chainlen
    rows = [''] * numRows
    for turn in range(turns + 1):
      for ir in range(numRows):
        subs = s[turn * chainlen:(turn + 1) * chainlen]
        rows[ir] += subs[ir:ir + 1] + (subs[chainlen - ir:chainlen - ir + 1],
                                       '')[ir == numRows - 1]
    print(rows)
    return ''.join(rows)


# print(Solution().convert('PAYPALISHIRING', 3))
