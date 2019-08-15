class Solution:
  """
  @param n: a integer, denote the number of teams
  @return: a string
  """

  def findContestMatch(self, n):
    # write your code here
    arr = [str(i) for i in range(1, n + 1)]
    while len(arr) > 1:
      arr2 = [
          '(%s,%s)' % (arr[i], arr[len(arr) - 1 - i])
          for i in range(len(arr) // 2)
      ]
      arr = arr2
    return arr[0]
