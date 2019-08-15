class Solution:
  """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

  def sortLetters(self, chars):
    # write your code here
    st = 0
    fl = len(chars) - 1
    while (st < fl):
      while (st < fl and 'a' <= chars[st] <= 'z'):
        st += 1
      while (st < fl and 'A' <= chars[fl] <= 'Z'):
        fl -= 1
      if (st < fl):
        chars[st], chars[fl] = chars[fl], chars[st]
