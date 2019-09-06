class Solution:
  """
  @param n: an integer
  @return: the number of '1's in the first N number in the magical string S
  """

  def magicalString(self, n):
    # write your code here
    if n == 0:
      return 0
    if n < 4:
      return 1
    arr = [1, 2, 2]
    ptr = 2
    while (len(arr) < n):
      cnt = arr[ptr]
      num = arr[-1] % 2 + 1
      arr.extend([num] * cnt)
      ptr += 1
    tot = 0
    for idx in range(n):
      tot += arr[idx] % 2
    return tot
