from collections import defaultdict


class Solution:
  """
  @param org: a permutation of the integers from 1 to n
  @param seqs: a list of sequences
  @return: true if it can be reconstructed only one or false
  """

  def sequenceReconstruction(self, org, seqs):
    # write your code here
    graph = defaultdict(list)
    orgs = len(org)
    if orgs == 1:
      return (all(seq == [] or seq == org for seq in seqs) and
              any(seq == org for seq in seqs))
    pos = {v: k for k, v in enumerate(org)}
    for seq in seqs:
      if len(seq) == 0:
        continue
      if not seq[0] in pos:
        return False
      for idx in range(1, len(seq)):
        try:
          if pos[seq[idx]] <= pos[seq[idx - 1]]:
            return False
        except KeyError:
          return False
        graph[seq[idx - 1]].append(seq[idx])
    for idx in range(len(org) - 1):
      if org[idx + 1] not in graph[org[idx]]:
        return False
    return True
