from collections import Counter


class Solution:
  """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """

  def leastInterval(self, tasks, n):
    # write your code here
    cnts = list(sorted(Counter(tasks).values(), reverse=True))
    bat = n + 1
    t = 0
    while (len(cnts) > 0):
      if max(cnts) == 1 and len(cnts) < bat:
        t += len(cnts)
      else:
        t += bat
      cnts = sorted(
          list(
              filter(lambda x: x > 0,
                     [x - 1 for x in cnts[:bat]] + cnts[bat:])),
          reverse=True)
    return t
