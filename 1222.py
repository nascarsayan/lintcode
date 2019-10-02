class Solution:
  """
  @param IP: the given IP
  @return: whether an input string is a valid IPv4 address or IPv6 address or neither
  """

  def validIPAddress(self, IP):
    # Write your code here
    try:
      ip4 = IP.split('.')
      ip6 = IP.split(':')
      if (len(ip4) == 4 and
          all(str(int(x)) == x and 0 <= int(x) < (1 << 8) for x in ip4)):
        return 'IPv4'
      if (len(ip6) == 8 and all(
          len(x) <= 4 and (len(x) == 0 or 0 <= int(x, 16) < (1 << 16))
          for x in ip6)):
        return 'IPv6'
      return 'Neither'
    except Exception:
      return 'Neither'


print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
