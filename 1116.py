import re
from collections import defaultdict


class Solution:
  """
  @param n: a integer
  @param logs: a list of integers
  @return: return a list of integers
  """

  def exclusiveTime(self, n, logs):
    # write your code here
    reg = re.compile('([0-9]+):((?:start|end)):([0-9]+)')
    stac, cnt = [], defaultdict(int)
    for log in logs:
      sidx, typ, stm = reg.match(log).group(1, 2, 3)
      idx, tm = int(sidx), int(stm)
      if typ == 'start':
        if len(stac) > 0:
          cnt[stac[-1][0]] += tm - stac[-1][1]
        stac.append([idx, tm])
      else:
        st = stac.pop(-1)
        cnt[int(idx)] += (tm + 1 - st[1])
        if len(stac) > 0:
          stac[-1][1] = tm + 1

    ks = sorted(cnt.keys())
    res = []
    for ke in ks:
      res.append(cnt[ke])
    return res


print(Solution().exclusiveTime(3, [
    '0:start:0', '1:start:2', '2:start:3', '2:end:4', '1:end:5', '0:end:6',
    '1:start:7', '1:end:10'
]))
