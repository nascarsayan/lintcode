class Solution:
  """
    @param n: The integer
    @return: Roman representation
    """

  def intToRoman(self, n):
    # write your code here
    rom = ''
    val2rom = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }
    weights = [1000, 500, 100, 50, 10, 5, 1]
    for idx, weight in enumerate(weights):
      while (n >= weight):
        rom += val2rom[weight]
        n -= weight
      if idx < len(weights) - 1:
        decweight = weights[idx + (1 + (idx + 1) % 2)]
        diffweight = weight - decweight
        if n >= diffweight:
          rom += val2rom[decweight] + val2rom[weight]
          n -= diffweight

    return rom


# print(Solution().intToRoman(3998))
