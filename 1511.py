class Solution:
  """
    @param p: an integer
    @param q: an integer
    @return: the number of the receptor that the ray meets first
    """

  def mirrorReflection(self, p, q):
    # Write your code here
    def hcf(p, q):
      while (p > 0):
        p, q = q % p, p
      return q

    lcm = (p * q) // hcf(p, q)
    if (lcm // p) % 2 == 0:
      return 0
    else:
      if (lcm // q) % 2 == 0:
        return 2
      else:
        return 1
