class Solution:
  """
  @param sentence: a list of string
  @param rows: an integer
  @param cols: an integer
  @return: return an integer, denote times the given sentence can be fitted on the screen
  """

  def wordsTyping(self, sentence, rows, cols):
    # Write your code here
    wds = list(map(len, sentence))
    ssize = len(sentence)
    if ssize == 0:
      return float('inf')
    if rows == 0 or cols == 0:
      return 0
    times = 0
    ir, ic = 0, 0
    curr = 0
    while (ir < rows):
      if ic + wds[curr] <= cols:
        ic += wds[curr]
        ir, ic = ir + (ic + 1) // cols, (ic + 1) % cols
        ic = (ic, 0)[ic == 1]
        curr += 1
        if curr == ssize:
          curr = 0
          times += 1
      else:
        ir, ic = ir + 1, 0
    return times
