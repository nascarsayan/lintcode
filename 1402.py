from collections import defaultdict


class Solution:
  """
    @param friends: people's friends
    @param user: the user's id
    @return: the person who most likely to know
    """

  def recommendFriends(self, friends, user):
    # Write your code here
    flists = defaultdict(set)
    flists[user] = set(friends[user])
    cnt = defaultdict(int)
    mx = -1
    for i in friends[user]:
      flists[i] = set(friends[i]).difference(flists[user]).difference(set(user))
      for fr in flists[i]:
        cnt[fr] += 1
        if mx == -1 or cnt[mx] < cnt[fr] or (cnt[mx] == cnt[fr] and fr < mx):
          mx = fr
    return mx
