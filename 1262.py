class Solution:
  """
  @param data: an array of integers
  @return: whether it is a valid utf-8 encoding
  """

  def validUtf8(self, data):
    # Write your code here
    bits = list(map(lambda x: '{:08b}'.format(x), data))
    size = len(bits)
    if size == 0:
      return False
    idx = 0
    print(bits)
    while (idx < size):
      if bits[idx][0] == '0':
        idx += 1
      else:
        sz = len((bits[idx].split('0'))[0])
        print(sz)
        if not (2 <= sz <= 4 and idx + sz <= size and
                all(bits[idx + sp][:2] == '10' for sp in range(1, sz))):
          return False
        idx += sz
    return True


print(Solution().validUtf8([197, 130, 1]))
