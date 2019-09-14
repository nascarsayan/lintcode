class Solution:
  """
  @param inp: an abstract file system
  @return: return the length of the longest absolute path to file
  """

  def lengthLongestPath(self, inp):
    # write your code here
    mx = 0
    lines = list(inp.split('\n'))
    for i in range(len(lines)):
      segs = lines[i].split('\t')
      lines[i] = (len(segs) - 1, segs[-1])
    stac = []
    for lev, nom in lines:
      while (len(stac) > lev):
        stac.pop(-1)
      stac.append(nom)
      if '.' in nom:
        mx = max(mx, len('/'.join(stac)))
    return mx
