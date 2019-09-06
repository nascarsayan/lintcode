class Solution:
  """
  @param k: Write your code here
  @return: the sum of first k even-length palindrome numbers
  """

  def sumKEven(self, k):
    #
    sm = list(map(lambda x: str(x), range(10)))
    arr = sm[1:]
    nums = list(map(lambda x: int(x + x[::-1]), arr))
    tk = k
    while (tk > len(arr)):
      arr2 = []
      for ea in arr:
        for es in sm:
          arr2.append(ea + es)
          nums.append(int(arr2[-1] + arr2[-1][::-1]))
      tk -= len(arr)
      arr = arr2
    return sum(nums[:k])


print(Solution().sumKEven(10))
