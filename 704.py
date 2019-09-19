class Solution:
  """
  @param n: number of lights
  @param m: number of operations
  @return: the number of status
  """

  def flipLights(self, n, m):
    # write your code here
    if m == 0 or n == 0:
      return 1
    if n == 1:
      return 2
    if n == 2:
      if m == 1:
        return 3
      return 4
    if m == 1:
      return 4
    if m == 2:
      return 7
    return 8

    # if m == 0:
    #   return ['on'] * n
    # res = []
    # res.append(['off'] * n)
    # res.append((['on', 'off'] * ((n + 1) // 2))[:n])
    # res.append((['off', 'on'] * ((n + 1) // 2))[:n])
    # res.append((['off', 'on', 'on'] * ((n + 2) // 3))[:n])
    # if m > 1:
    #   res.append((['on', 'off', 'off'] * ((n + 2) // 3))[:n])
    #   res.append((['on', 'on', 'on', 'off', 'off', 'off'] *
    #               ((n + 1 + 5) // 6))[1:n + 1])
    #   res.append((['off', 'off', 'off', 'on', 'on', 'on'] *
    #               ((n + 1 + 5) // 6))[1:n + 1])
    # if n <= 3:
    #   res = list(map(list, set(map(tuple, res))))
    # return res


print(Solution().flipLights(3, 2))
