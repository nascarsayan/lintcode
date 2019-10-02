class Solution:
  """
  @param A: an array
  @param S: the sum
  @return: the number of non-empty subarrays
  """

  def numSubarraysWithSum(self, A, S):
    # Write your code here.
    if S == 0:
      return sum(
          list(
              map(lambda x: (len(x) * (len(x) + 1)) // 2,
                  (''.join(list(map(str, A)))).split('1'))))
    idcs = [-1] + list([i for i, v in enumerate(A) if v == 1]) + [len(A)]
    res = 0
    for fl in range(S, len(idcs) - 1):
      res += (idcs[fl - S + 1] - idcs[fl - S]) * (idcs[fl + 1] - idcs[fl])
    return res


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))
