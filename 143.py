class Solution:
  """
  @param colors: A list of integer
  @param k: An integer
  @return: nothing
  """

  def sortColors2(self, colors, k):
    # write your code here
    cnt = [0] * (k + 1)
    for col in colors:
      cnt[col] += 1
    res = []
    for i in range(1, k + 1):
      res.extend([i] * cnt[i])
    for i in range(len(colors)):
      colors[i] = res[i]


print(Solution().sortColors2([], 0))
