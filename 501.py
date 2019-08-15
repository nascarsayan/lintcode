from collections import defaultdict
'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''


class Tweet:

  @classmethod
  def create(cls, user_id, tweet_text):
    # This will create a new tweet object,
    # and auto fill id
    return


class MiniTwitter:

  def __init__(self):
    # do intialization if necessary
    self.tweets = defaultdict(list)
    self.fdlist = defaultdict(set)
    self.idv = 0

  """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """

  def postTweet(self, user_id, tweet_text):
    # write your code here
    t = Tweet.create(user_id, tweet_text)
    self.tweets[user_id].append((self.idv, t))
    self.idv += 1
    return t

  """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """

  def getNewsFeed(self, user_id):
    # write your code here
    tw = self.tweets[user_id][-10:]
    for f in self.fdlist[user_id]:
      tw.extend(self.tweets[f][-10:])
    tw.sort(key=lambda x: x[0])
    return list(map(lambda x: x[1], tw[-10:][::-1]))

  """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """

  def getTimeline(self, user_id):
    # write your code here
    return list(map(lambda x: x[1], self.tweets[user_id][-10:][::-1]))

  """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

  def follow(self, from_user_id, to_user_id):
    # write your code here
    self.fdlist[from_user_id].add(to_user_id)

  """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

  def unfollow(self, from_user_id, to_user_id):
    # write your code here
    self.fdlist[from_user_id].remove(to_user_id)
