class Solution:
  """
  @param st: a string
  @return: return a string
  """

  def reverseWords(self, st):
    # write your code here
    return ' '.join(reversed(st.split(' ')))
