class Solution:
  """
  @param values: a vector of integers
  @return: a boolean which equals to true if the first player will win
  """

  def firstWillWin(self, values):
    # write your code here
    size = len(values)
    if size < 3:
      return True
    values = values[::-1]
    tot = [0]
    for i in range(size):
      tot.append(tot[-1] + values[i])
    tot.pop(0)
    mx = [tot[0], tot[1]]
    for i in range(2, size):
      mx.append(
          max(values[i] + tot[i - 1] - mx[-1],
              values[i] + values[i - 1] + tot[i - 2] - mx[-2]))
    return mx[-1] * 2 >= tot[-1]


print(Solution().firstWillWin([100, 200, 400, 300, 400, 800, 500, 600, 1200]))
