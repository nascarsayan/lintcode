from collections import deque


class Solution:
  """
  @param A: The prices [i]
  @param k:
  @return: The ans array
  """

  def business(self, A, k):
    # Write your code here
    k = abs(k)
    que = deque()
    size = len(A)
    mn = A[:]
    for i in range(size):
      while (que and A[que[-1]] >= A[i]):
        que.pop()
      que.append(i)
      if que[0] < i - k:
        que.popleft()
      mn[i] = min(mn[i], A[que[0]])
    que = deque()
    for i in range(size)[::-1]:
      while (que and A[que[0]] >= A[i]):
        que.popleft()
      que.appendleft(i)
      if que[-1] > i + k:
        que.pop()
      mn[i] = min(mn[i], A[que[-1]])
    return list(map(lambda x: x[0] - x[1], list(zip(A, mn))))
