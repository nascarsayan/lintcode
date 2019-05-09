class Solution:
  """
  @param n: An integer
  @return: A list of strings.
  """
  def fizzBuzz(self, n):
    # write your code here
    arr = []
    for i in range(1, n + 1):
      if (i % 3 == 0 and i % 5 == 0):
        arr.append("fizz buzz")
      elif (i % 3 == 0):
        arr.append("fizz")
      elif (i % 5 == 0):
        arr.append("buzz")
      else:
        arr.append(str(i))
    return arr
