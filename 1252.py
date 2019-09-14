class Solution:
  """
    @param people: a random list of people
    @return: the queue that be reconstructed
    """

  def reconstructQueue(self, people):
    # write your code here
    que = []
    people.sort(key=lambda x: (-x[0], x[1]))
    for person in people:
      que.insert(person[1], person)
    return que


print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1],
                                   [5, 2]]))
