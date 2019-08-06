class Solution:
  """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

  def kClosestNumbers(self, A, target, k):
    # write your code here
    size = len(A)
    kcl = []
    if k == 0 or size == 0:
      return kcl
    st = 0
    fl = size - 1
    mid = None
    while (st <= fl):
      mid = (st + fl) >> 1
      if A[mid] == target:
        break
      if A[mid] < target:
        st = mid + 1
      else:
        fl = mid - 1
    if st > fl:
      if st >= size:
        mid = size - 1
      elif fl < 0:
        mid = 0
      else:
        mid = (fl, st)[abs(A[st] - target) < abs(A[fl] - target)]
    kcl.append(A[mid])
    k -= 1
    st = mid - 1
    fl = mid + 1
    while ((st >= 0 or fl < size) and k > 0):
      if (st < 0):
        kcl.append(A[fl])
        fl += 1
      elif (fl >= size):
        kcl.append(A[st])
        st -= 1
      else:
        val, st, fl = ((A[st], st - 1, fl),
                       (A[fl], st,
                        fl + 1))[abs(A[fl] - target) < abs(A[st] - target)]
        kcl.append(val)
      k -= 1
    return kcl
