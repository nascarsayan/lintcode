class Solution:
  """
  @param timeSeries: the Teemo's attacking ascending time series towards Ashe
  @param duration: the poisoning time duration per Teemo's attacking
  @return: the total time that Ashe is in poisoned condition
  """

  def findPoisonedDuration(self, timeSeries, duration):
    # Write your code here
    tot = 0
    size = len(timeSeries)
    for idx in range(1, size):
      tot += min(timeSeries[idx] - timeSeries[idx - 1], duration)
    if size > 0:
      tot += duration
    return tot
