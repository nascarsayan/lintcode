class Solution:
  """
  @param people: The i-th person has weight people[i].
  @param limit: Each boat can carry a maximum weight of limit.
  @return: Return the minimum number of boats to carry every given person. 
  """

  def numRescueBoats(self, people, limit):
    # Write your code here.
    people.sort()
    st, fl = 0, len(people) - 1
    nboat = 0
    while (st < fl):
      if people[st] + people[fl] <= limit:
        st += 1
      fl -= 1
      nboat += 1
    if st == fl:
      nboat += 1
    return nboat
