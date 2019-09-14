class Solution:
  """
    @param ghosts: a 2D integer array
    @param target: a integer array
    @return: return boolean
    """

  def escapeGhosts(self, ghosts, target):
    # write your code here
    return all(
        abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) > abs(target[0]) +
        abs(target[1]) for ghost in ghosts)
