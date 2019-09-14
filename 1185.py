class Solution:
  """
  @param a: a string
  @param b: a string
  @return: a string representing their multiplication
  """

  def complexNumberMultiply(self, a, b):
    # Write your code here
    ar, ac = a.split('+')
    br, bc = b.split('+')
    ar, br, ac, bc = int(ar), int(br), int(ac[:-1]), int(bc[:-1])
    resr = ar * br - ac * bc
    resc = ar * bc + br * ac
    return '{}+{}i'.format(resr, resc)
