class Solution:
  """
  @param num: the number of "1"s on a given timetable
  @return: all possible time
  """

  def binaryTime(self, num):
    # Write your code here
    def recurse(cnt, hr, mn, pos):
      if hr > 11 or mn > 59 or pos > 6 or cnt < 0:
        return
      if cnt == 0:
        poss.append('%d:%02d' % (hr, mn))
        return
      recurse(cnt - 1, hr + (1 << pos), mn, pos + 1)
      recurse(cnt - 1, hr, mn + (1 << pos), pos + 1)
      recurse(cnt - 2, hr + (1 << pos), mn + (1 << pos), pos + 1)
      recurse(cnt, hr, mn, pos + 1)

    poss = []
    recurse(num, 0, 0, 0)
    return poss
