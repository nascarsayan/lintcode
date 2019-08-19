class Solution:
  """
  @param N: an integer
  @return: how many ways can we write it as a sum of consecutive positive integers
  """

  def consecutiveNumbersSum(self, N):
    # Write your code here
    lim = int((1 + pow(1 + 8 * N, 0.5)) / 2 + 1)
    s = 0
    ty = 0
    for n in range(lim + 1):  # n is the number of integers in the sequence
      s += (n + 1)
      if (N - s) < 0:
        break
      if (N - s) % (n + 1) == 0:
        ty += 1
    return ty
