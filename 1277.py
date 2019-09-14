class Solution:
  """
  @param x: the given number x
  @param y: the given number y
  @param z: the given number z
  @return: whether it is possible to measure exactly z litres using these two jugs
  """

  def canMeasureWater(self, x, y, z):
    # Write your code here
    def hcf(x, y):
      while (x > 0):
        x, y = y % x, x
      return y

    if not 0 <= z <= x + y:
      return False
    gcd = hcf(x, y)
    return z % gcd == 0


print(Solution().canMeasureWater(104707, 104711, 1))
