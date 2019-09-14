class Solution:
  """
  @param time: the given time
  @return: the next closest time
  """

  def nextClosestTime(self, time):
    # write your code here
    tm = [int(time[i]) for i in [0, 1, 3, 4]]
    digs = list(sorted(set(tm)))
    size = len(digs)
    mx6 = digs[0]
    mx4 = digs[0]
    for idx in range(1, size):
      if digs[idx] < 6:
        mx6 = digs[idx]
      if digs[idx] < 4:
        mx4 = digs[idx]
    mx2 = digs[0]
    if len(digs) > 1 and digs[1] < 2:
      mx2 = digs[1]
    if tm[-1] < digs[-1]:
      for idx in range(1, size):
        if digs[idx] > tm[-1]:
          tm[-1] = digs[idx]
          break
    elif tm[-2] < mx6:
      for idx in range(1, size):
        if digs[idx] > tm[-2]:
          tm[-2] = digs[idx]
          tm[-1] = digs[0]
          break
    elif tm[-3] < (digs[-1], mx4)[digs[0] == 2]:
      for idx in range(1, size):
        if digs[idx] > tm[-3]:
          tm[-3] = digs[idx]
          tm[-2] = tm[-1] = digs[0]
          break
    elif tm[-4] < mx2:
      tm[-4] = mx2
      tm[-3] = tm[-2] = tm[-1] = digs[0]
    else:
      tm[-4] = tm[-3] = tm[-2] = tm[-1] = digs[0]
    return '{}{}:{}{}'.format(tm[0], tm[1], tm[2], tm[3])


print(Solution().nextClosestTime("22:22"))
