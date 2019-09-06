from functools import cmp_to_key
from decimal import Decimal, getcontext
import math


class Solution:

  def getArray(self, A, target):

    def mycmp(x, y):
      if x[1] != y[1]:
        return x[1] - y[1]
      return y[0] - x[0]

    getcontext().prec = 3
    fracs = list(
        sorted(
            enumerate(list(map(lambda x: Decimal(int(x + 1)) - Decimal(x), A))),
            key=cmp_to_key(mycmp)))
    # print(fracs)
    tot = sum(list(map(lambda x: int(x), A)))
    for i in range(target - tot):
      A[fracs[i][0]] += 1
    return list(map(lambda x: math.floor(x), A))
