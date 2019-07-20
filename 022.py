# https://www.lintcode.com/problem/flatten-list/

class Solution(object):

  # @param nestedList a list, each element in the list 
  # can be a list or integer, for example [1,2,[1,2]]
  # @return {int[]} a list of integer
  def flatten(self, nestedList):
    # Write your code here
    if (type(nestedList) is not list):
      return [nestedList]
    flat = []
    for el in nestedList:
      if (type(el) is list):
        flat += self.flatten(el)
      else:
        flat += [el]
    return flat

# print(Solution().flatten([4,[3,[2,[1]]]]))
