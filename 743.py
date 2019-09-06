class Solution:
  """
  @param num: a non-negative integer N
  @return: the largest number that is less than or equal to N with monotone increasing digits.
  """

  def monotoneDigits(self, num):
    # write your code here
    digs = list(str(num))
    size = len(digs)
    idx = 1
    while (idx < size and digs[idx] >= digs[idx - 1]):
      idx += 1
    if idx == size:
      return num
    idx -= 1
    while (idx > 0 and digs[idx] == digs[idx - 1]):
      idx -= 1
    digs[idx] = chr(ord(digs[idx]) - 1)
    idx += 1
    while (idx < size):
      digs[idx] = '9'
      idx += 1
    return int(''.join(digs))


print(Solution().monotoneDigits(123453))
