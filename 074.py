# class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.


class SVNRepo:

  @classmethod
  def isBadVersion(cls, id):
    return 0


class Solution:
  """
    @param n: An integer
    @return: An integer which is the first bad version.
    """

  def findFirstBadVersion(self, n):
    # write your code here
    repo = SVNRepo()
    isBad = {n: repo.isBadVersion(n)}
    if n == 0 or not isBad[n]:
      return 0
    if n > 1:
      isBad[1] = repo.isBadVersion(1)
    if isBad[1]:
      return 1
    if n == 1:
      return 0

    st = 1
    fl = n - 1
    while (st <= fl):
      mid = (st + fl) >> 1
      if mid not in isBad:
        isBad[mid] = repo.isBadVersion(mid)
      if mid + 1 not in isBad:
        isBad[mid + 1] = repo.isBadVersion(mid + 1)
      if not isBad[mid] and isBad[mid + 1]:
        return mid + 1
      if isBad[mid]:
        fl = mid
      else:
        st = mid + 1
    return 0
