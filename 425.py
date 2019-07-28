class Solution:
  """
    @param digits: A digital string
    @return: all posible letter combinations
    """

  def __init__(self):
    self.alphs = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

  def recurse(self, digits, ndig, idx, currs, permut):
    if idx == ndig:
      permut.append(currs)
      return
    for a in self.alphs[digits[idx]]:
      self.recurse(digits, ndig, idx + 1, currs + a, permut)

  def letterCombinations(self, digits):
    # write your code here
    if len(digits) == 0:
      return []
    permut = []
    try:
      self.recurse(digits, len(digits), 0, '', permut)
    except Exception:
      return []
    return permut


# print(Solution().letterCombinations('23'))
