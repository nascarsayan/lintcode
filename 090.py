class Solution:
  """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

  def kSumII(self, A, k, target):
    # write your code here

    def recurse(path, idx):
      tot = sum(path) or 0
      sz = len(path)
      if sz == k and tot == target:
        poss.append(path)
        return
      if idx >= len(A) or tot > target or sz > k:
        return
      recurse(path + [A[idx]], idx + 1)
      recurse(path, idx + 1)

    A.sort()
    poss = []
    if target == 0:
      return poss
    recurse([], 0)
    return poss
