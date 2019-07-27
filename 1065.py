class MyCalendar:

  def __init__(self):
    self.invs = []

  def book(self, start, end):
    """
    :type start: int
    :type end: int
    :rtype: bool
    """
    arr = self.invs
    l = len(arr)
    if l == 0 or start >= end:
      arr.append([start, end])
      return True
    st = 0
    fl = l - 1
    idx = None
    while (st <= fl):
      mid = (st + fl) // 2
      if (start < arr[mid][1] and end > arr[mid][0]):
        return False
      if start >= arr[mid][1]:
        if (mid == l - 1 or end <= arr[mid + 1][0]):
          idx = mid + 1
          break
        st = mid + 1
      elif end <= arr[mid][0]:
        if (mid == 0 or start >= arr[mid - 1][1]):
          idx = mid
          break
        fl = mid - 1
    if idx is None:
      return False
    arr.insert(idx, [start, end])
    return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(10, 20)
# param_2 = obj.book(15, 25)
# param_3 = obj.book(20, 30)
# print(param_1)
# print(param_2)
# print(param_3)