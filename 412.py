class Solution:
  """
  @param ratings: Children's ratings
  @return: the minimum candies you must give
  """

  def candy(self, ratings):
    # write your code here
    size = len(ratings)
    if size == 0:
      return 0
    if size == 1:
      return 1
    chocos = [None] * size
    chocos[0] = 1
    degidx = None
    for idx in range(1, size):
      if ratings[idx] >= ratings[idx - 1]:
        if degidx is not None:
          if chocos[idx - 1] < 1:
            for idx2 in range(degidx, idx):
              chocos[idx2] += 1 - chocos[idx - 1]
          if chocos[idx - 1] > 1:
            for idx2 in range(idx - 1, degidx, -1):
              chocos[idx2] = idx - idx2
        degidx = None
        if ratings[idx] > ratings[idx - 1]:
          chocos[idx] = chocos[idx - 1] + 1
        else:
          chocos[idx] = 1
      else:
        if degidx is None:
          degidx = idx - 1
        chocos[idx] = chocos[idx - 1] - 1
    if degidx is not None:
      if chocos[-1] < 1:
        for idx2 in range(degidx, size):
          chocos[idx2] += 1 - chocos[-1]
      if chocos[size - 1] > 1:
        for idx2 in range(size - 1, degidx, -1):
          chocos[idx2] = size - idx2
    print(chocos)
    return sum(chocos)


# print(Solution().candy([4, 2, 3, 4, 1]))
