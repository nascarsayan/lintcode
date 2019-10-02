class Solution:

  def __init__(self):
    self.dic = {}

  def encode(self, longUrl):
    # Encodes a URL to a shortened URL.
    encoded = str(id(longUrl))
    self.dic[encoded] = longUrl
    return 'http://nascarsayan.com/' + encoded

  def decode(self, shortUrl):
    # Decodes a shortened URL to its original URL.
    return self.dic[(shortUrl.split('/'))[-1]]


# Your Codec object will be instantiated and called as such:
# Codec codec = new Codec();
# codec.decode(codec.encode(url));
