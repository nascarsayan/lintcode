class Solution:
  """
  @param n: an integer
  @param k: an integer
  @return: how many problem can you accept
  """

  def canAccept(self, n, k):
    # Write your code here
    return int((-1 + ((1 + (8 * n) / k)**0.5)) / 2)
