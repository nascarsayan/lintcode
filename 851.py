class Solution:
  """
    @param heights: the height of the terrain
    @param V: the units of water
    @param K: the index
    @return: how much water is at each index
    """

  def pourWater(self, heights, V, K):
    # Write your code here
    size = len(heights)
    for _ in range(V):
      left = K
      right = K
      while (left > 0 and heights[left - 1] <= heights[left]):
        left -= 1
      while (left < K and heights[left + 1] == heights[left]):
        left += 1
      while (right < size - 1 and heights[right + 1] <= heights[right]):
        right += 1
      while (right > K and heights[right - 1] == heights[right]):
        right -= 1
      if heights[left] < heights[K]:
        heights[left] += 1
      else:
        heights[right] += 1
    return heights


print(Solution().pourWater([13, 7, 9, 6, 4, 4, 4, 10, 15, 9], 7, 1))

# !Failed attempt
# def pourWater(self, heights, V, K):
#   # Write your code here
#   def popustac(left, right):
#     if left is not None:
#       for i in range(left - 1, -1, -1):
#         if heights[i] > heights[i + 1]:
#           break
#         if heights[i] < heights[i + 1]:
#           lstac.append(i)
#     if right is not None:
#       for i in range(right + 1, size):
#         if heights[i] >= heights[i - 1]:
#           break
#         if heights[i] < heights[i - 1]:
#           rstac.append(i)

#   lstac = [K]
#   rstac = [K]
#   size = len(heights)

#   popustac(left=K, right=K)
#   while (V > 0):
#     if len(lstac) > 1:
#       lm = lstac[-1]
#       heights[lm] += 1
#       V -= 1
#       if (heights[lm] == heights[lstac[-2]] or
#           (lm > 0 and heights[lm - 1] <= heights[lm])):
#         li = lstac.pop(-1)
#         popustac(left=li, right=None)
#     elif len(rstac) > 1:
#       rm = rstac[-1]
#       heights[rm] += 1
#       V -= 1
#       if (heights[rm] == heights[rstac[-2]] or
#           (rm < size - 1 and heights[rm + 1] <= heights[rm])):
#         ri = rstac.pop(-1)
#         popustac(left=None, right=ri)
#     if (len(lstac) == 1 and len(rstac) == 1):
#       popustac(left=K, right=K)
#     if (len(lstac) == 1 and len(rstac) == 1):
#       heights[K] += 1
#       V -= 1
#   return heights