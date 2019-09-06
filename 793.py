class Solution:
  """
  @param arrs: the arrays
  @return: the number of the intersection of the arrays
  """

  def intersectionOfArrays(self, arrs):
    # write your code here
    size = len(arrs)
    if size == 0:
      return 0
    insc = set(arrs[0])
    for arr in arrs[1:]:
      insc.intersection_update(set(arr))
    return len(insc)
