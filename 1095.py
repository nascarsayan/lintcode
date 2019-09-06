class Solution:
  """
  @param num: a non-negative intege
  @return: the maximum valued number
  """

  def maximumSwap(self, num):
    # Write your code here
    sn = list(str(num))
    size = len(sn)
    idx = 1
    while (idx < size):
      if sn[idx] > sn[idx - 1]:
        break
      idx += 1
    if idx >= size:
      return num
    st, fl = idx - 1, idx
    mx = fl
    while (fl < size):
      if sn[fl] >= sn[mx]:
        mx = fl
      fl += 1
    while (st >= 0 and sn[st] < sn[mx]):
      st -= 1
    st += 1
    sn[st], sn[mx] = sn[mx], sn[st]
    return int(''.join(sn))
