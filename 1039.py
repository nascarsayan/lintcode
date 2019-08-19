class Solution:
  """
  @param arr: a permutation of N
  @return: the most number of chunks
  """

  def maxChunksToSorted(self, arr):
    # write your code here
    tot = 0
    chunk = 0
    for fl in range(len(arr)):
      tot += arr[fl]
      if tot == (fl * (fl + 1)) // 2:
        chunk += 1
    return chunk
