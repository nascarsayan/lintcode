class Solution:
  """
  @param timePoints: a list of 24-hour clock time points
  @return: the minimum minutes difference between any two time points in the list
  """

  def findMinDifference(self, timePoints):
    # Write your code here
    minutes = sorted(
        list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints)))
    mn = (minutes[0] - minutes[-1]) % (60 * 24)
    for i in range(1, len(minutes)):
      mn = min(mn, minutes[i] - minutes[i - 1])
    return mn
