class Solution:
  """
  @param difficulty:
  @param profit:
  @param worker:
  @return: nothing
  """

  def maxProfitAssignment(self, difficulty, profit, worker):
    jobs = list(zip(difficulty, profit))
    jobs.sort()
    ans = i = best = 0
    for skill in sorted(worker):
      while i < len(jobs) and skill >= jobs[i][0]:
        best = max(best, jobs[i][1])
        i += 1
      ans += best
    return ans


print(Solution().maxProfitAssignment([23, 43, 3], [10, 13, 28],
                                     [19, 43, 33, 17]))
