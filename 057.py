class Solution:
  """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

  def threeSum(self, numbers):
    # write your code here
    trips = []
    size = len(numbers)
    if (size < 3):
      return trips
    numbers.sort()
    i = 0
    while (i < size - 2):
      if (numbers[i] == numbers[i + 1]):
        if (numbers[i + 1] == numbers[i + 2]):
          if numbers[i] == 0:
            trips.append([0] * 3)
        else:
          thr = -(numbers[i] + numbers[i + 1])
          if thr in numbers[i + 2:]:
            trips.append([numbers[i]] * 2 + [thr])
        while (numbers[i] == numbers[i + 1] and i < size - 2):
          i += 1
        continue
      st = i + 1
      fl = size - 1
      while (st < fl):
        sumv = numbers[i] + numbers[st] + numbers[fl]
        if sumv == 0:
          trips.append([numbers[idx] for idx in [i, st, fl]])
        if sumv < 0:
          st += 1
        elif sumv > 0:
          fl -= 1
        else:
          while (numbers[st + 1] == numbers[st] and st < fl):
            st += 1
          while (numbers[fl - 1] == numbers[fl] and st < fl):
            fl -= 1
          st += 1
      i += 1
    return trips


# !Cheat using set
# class Solution:
#   """
#     @param numbers: Give an array numbers of n integer
#     @return: Find all unique triplets in the array which gives the sum of zero.
#     """

#   def threeSum(self, numbers):
#     # write your code here
#     trips = set()
#     size = len(numbers)
#     if (size < 3):
#       return list(trips)
#     numbers.sort()
#     for i in range(size - 2):
#       st = i + 1
#       fl = size - 1
#       while (st < fl):
#         sumv = numbers[i] + numbers[st] + numbers[fl]
#         if sumv == 0:
#           trips.add((numbers[i], numbers[st], numbers[fl]))
#         if sumv < 0:
#           st += 1
#         elif sumv > 0:
#           fl -= 1
#         else:
#           if numbers[st + 1] == numbers[st]:
#             st += 1
#           else:
#             fl -= 1
#     return list(map(list, trips))
