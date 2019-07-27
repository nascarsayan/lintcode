class MyQueue:

  def __init__(self):
    # do intialization if necessary
    self.que1 = []
    self.que2 = []

  """
  @param: element: An integer
  @return: nothing
  """

  def push(self, element):
    # write your code here
    self.que1.append(element)

  """
  @param: q1: Non-empty container
  @param: q2: Empty container
  @return: nothing
  """

  def pour(self, q1, q2):
    l1 = len(q1)
    l2 = len(q2)
    if (l2 > 0):
      return
    while (l1 > 0):
      q2.append(q1.pop())
      l1 -= 1

  """
  @return: An integer
  """

  def pop(self):
    # write your code here
    self.pour(self.que1, self.que2)
    return self.que2.pop()

  """
  @return: An integer
  """

  def top(self):
    # write your code here
    self.pour(self.que1, self.que2)
    return self.que1[-1]