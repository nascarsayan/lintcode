class Solution:
  """
  @param n: An integer
  @param stri: a string with number from 1-n in random order and miss one number
  @return: An integer
  """

  def findMissing2(self, n, stri):
    # write your code here
    def dfs(idx):
      if idx == size:
        for i in range(1, n + 1):
          if not visited[i]:
            mis[0] = i
        return True
      d1 = int(stri[idx])
      if d1 > 0 and not visited[d1]:
        visited[d1] = True
        fl = dfs(idx + 1)
        visited[d1] = False
        if fl:
          return True
      if idx < size - 1:
        d2 = int(stri[idx:idx + 2])
        if 1 <= d2 <= n and str(d2) == stri[idx:idx + 2] and not visited[d2]:
          visited[d2] = True
          fl = dfs(idx + 2)
          visited[d2] = False
          if fl:
            return True
      return False

    mis = [None]
    size = len(stri)
    visited = [False] * (n + 1)
    dfs(0)
    return mis[0]


print(Solution().findMissing2(11, "111098765432"))
