class CircularQueue:

  def __init__(self, n):
    # do intialization if necessary
    self.que = []
    self.n = n

  """
    @return:  return true if the array is full
    """

  def isFull(self):
    # write your code here
    return len(self.que) == self.n

  """
    @return: return true if there is no element in the array
    """

  def isEmpty(self):
    # write your code here
    return len(self.que) == 0

  """
    @param element: the element given to be added
    @return: nothing
    """

  def enqueue(self, element):
    # write your code here
    self.que.append(element)

  """
    @return: pop an element from the queue
    """

  def dequeue(self):
    # write your code here
    return self.que.pop(0)
