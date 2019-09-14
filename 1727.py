class Solution:
  """
  @param A:
  @return: return an integer
  """

  def partitionDisjoint(self, A):
    # write your code here
    size = len(A)
    mn, mx = [A[-1]], [A[0]]
    for i in range(size - 1)[::-1]:
      mn.append(min(mn[-1], A[i]))
    mn.reverse()
    for i in range(1, size):
      mx.append(max(mx[-1], A[i]))
    # print(mn)
    # print(mx)
    for i in range(size - 1):
      if mx[i] <= mn[i + 1]:
        return i + 1
    return size


print(Solution().partitionDisjoint([5, 0, 3, 8, 6]))
