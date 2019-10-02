class Solution:
  """
  @param dominoes: a string
  @return: a string representing the final state
  """

  def pushDominoes(self, dominoes):
    # Write your code here
    impe = []
    dominoes = list(dominoes)
    for i, domino in enumerate(dominoes):
      if domino == 'L':
        impe.append((i, -1))
      elif domino == 'R':
        impe.append((i, 1))
    size, idx = len(impe), 0
    while (idx < size):
      i, wt = impe[idx]
      if wt == -1:
        j = i - 1
        while (j >= 0 and dominoes[j] == '.'):
          dominoes[j] = 'L'
          j -= 1
      else:
        if idx == size - 1 or impe[idx + 1][1] == 1:
          j = i + 1
          while (j < len(dominoes)):
            if dominoes[j] != '.':
              break
            dominoes[j] = 'R'
            j += 1
        else:
          st, fl = impe[idx][0], impe[idx + 1][0]
          while (st < fl):
            dominoes[st], dominoes[fl] = 'R', 'L'
            st, fl = st + 1, fl - 1
          idx += 1
      idx += 1
    return ''.join(dominoes)


print(Solution().pushDominoes(".L.R."))
