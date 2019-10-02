import os
from collections import defaultdict


class Solution:
  """
  @param paths: a list of string
  @return: all the groups of duplicate files in the file system in terms of their paths
  """

  def findDuplicate(self, paths):
    # Write your code here
    c2p = defaultdict(list)
    for path in paths:
      info = path.split()
      par = info[0]
      for fc in info[1:]:
        file, cont = fc.split('(')
        c2p[cont[:-1]].append(os.path.join(par, file))
    res = []
    for v in c2p.values():
      if len(v) > 1:
        res.append(v)
    return res


print(Solution().findDuplicate([
    "root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"
]))
