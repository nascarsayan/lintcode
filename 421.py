class Solution:
  """
  @param path: the original path
  @return: the simplified path
  """

  def simplifyPath(self, path):
    # write your code here
    if path[0] != '/':
      return None
    tokens = path.split('/')
    michi = []
    for token in tokens:
      if len(token) == 0 or token == '.':
        continue
      elif token == '..':
        if len(michi) > 0:
          michi.pop(-1)
      else:
        michi.append(token)
    return '/' + '/'.join(michi)


# print(Solution().simplifyPath('/a/./../../c/'))
