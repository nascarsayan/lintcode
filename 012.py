# https://www.lintcode.com/problem/min-stack/

class MinStack:
  
  def __init__(self):
    # do intialization if necessary
    self.arr = []
    self.minval = None

  """
  @param: number: An integer
  @return: nothing
  """
  def push(self, number):
    # write your code here
    if (self.minval == None):
      self.minval = number
      self.arr.append(number)
    elif (self.minval > number):
      self.arr.append(2 * number - self.minval)
      self.minval = number
    else:
      self.arr.append(number)

  """
  @return: An integer
  """
  def pop(self):
    # write your code here
    try:
      v = self.arr.pop()
      if (v < self.minval):
        v, self.minval = self.minval, 2 * self.minval - v
      if (len(self.arr) == 0):
        self.minval = None
      return v
    except:
      return None

  """
  @return: An integer
  """
  def min(self):
    # write your code here
    return self.minval

ms = MinStack()
ms.push(1)
print(ms.pop())
ms.push(2)
ms.push(3)
print(ms.min())
ms.push(1)
print(ms.min())
