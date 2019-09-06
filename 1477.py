class Solution:
  """
  @param target: the target
  @param position: the initial position
  @param speed: the speed
  @return: How many car fleets will arrive at the destination
  """

  def carFleet(self, target, position, speed):
    # Write your code here
    xu = sorted(zip(position, speed), key=lambda x: x[0])
    tm = list(map(lambda x: (target - x[0]) / x[1], xu))
    size = len(tm)
    if size < 1:
      return 0
    stac = []
    for etm in tm:
      while (len(stac) > 0 and stac[-1] <= etm):
        stac.pop(-1)
      stac.append(etm)
    return len(stac)


print(Solution().carFleet(13, [10, 2, 5, 7, 4, 6, 11], [7, 5, 10, 5, 9, 4, 1]))
