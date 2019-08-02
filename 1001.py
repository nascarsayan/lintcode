class Solution:
  """
    @param asteroids: a list of integers
    @return: return a list of integers
    """

  def asteroidCollision(self, asteroids):
    # write your code here
    stac = []
    for ast in asteroids:
      ob = ast
      while (len(stac) > 0 and stac[-1] > 0 and ob is not None and ob < 0):
        if stac[-1] > -ob:
          ob = None
        elif stac[-1] < -ob:
          stac.pop(-1)
        else:
          stac.pop(-1)
          ob = None
      if ob is not None:
        stac.append(ob)
    return stac


# print(Solution().asteroidCollision([10, 2, -5]))
