class Solution:
  """
  @param n: a non-negative integer
  @return: number of numbers with unique digits
  """

  def __init__(self):
    # self.uniq = [1, 9, 81]
    # for i in range(1, 9)[::-1]:
    #   self.uniq.append(self.uniq[-1] * i)
    # for i in range(1, len(self.uniq)):
    #   self.uniq[i] += self.uniq[i - 1]
    self.uniq = [
        1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691
    ]

  def countNumbersWithUniqueDigits(self, n):
    # Write your code here
    return self.uniq[min(n, 10)]


print(Solution())
