class Solution:
  """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

  def getTill(self, arr, target):
    if (len(arr) == 0):
      return 0
    m = len(arr)
    st = 0
    fl = m - 1
    till = None
    mid = st
    while (st < fl):
      mid = (st + fl) // 2
      if arr[mid] == target:
        till = mid
        break
      if arr[mid] < target:
        st = mid + 1
      else:
        fl = mid - 1
    if till is None:
      if arr[st] <= target:
        till = st
      else:
        till = st - 1
    return till

  def searchMatrix(self, matrix, target):
    # write your code here
    if (len(matrix) == 0 or len(matrix[0]) == 0):
      return 0
    till = self.getTill([x[0] for x in matrix], target)
    cnt = 0
    for curr in range(till + 1):
      pos = self.getTill(matrix[curr], target)
      if (pos >= 0 and matrix[curr][pos] == target):
        cnt += 1
    return cnt


# print(Solution().searchMatrix([[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]], 3))
