# Re
# !TLE


class Solution:
  """
  @param board: A list of lists of character
  @param word: A string
  @return: A boolean
  """

  def exist(self, board, word):
    # write your code here
    def recurse(word, i, j):
      if word == '':
        return True
      if (not (0 <= i < nr and 0 <= j < nc) or board[i][j] != word[0] or
          visited[i][j]):
        return False
      visited[i][j] = True
      flag = any(
          recurse(word[1:], i + di, j + dj)
          for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)])
      # if (recurse(word[1:], i, j - 1)):
      #   return True
      # if (recurse(word[1:], i - 1, j)):
      #   return True
      # if (recurse(word[1:], i, j + 1)):
      #   return True
      # if (recurse(word[1:], i + 1, j)):
      #   return True
      visited[i][j] = False
      return flag

    nr = len(board)
    nc = len(board[0])
    if len(word) == 0:
      return True
    if nr == 0 or nc == 0:
      return False
    for ir in range(nr):
      for ic in range(nc):
        visited = [[False] * nc for _ in range(nr)]
        if (recurse(word, ir, ic)):
          return True
    return False


print(Solution().exist(['ABCE', 'SFCS', 'ADEE'], 'ABCCED'))
