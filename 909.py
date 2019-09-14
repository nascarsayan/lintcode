class Solution:
  """
  @param m: an integer
  @param n: an integer
  @return: the total number of unlock patterns of the Android lock screen
  """

  def numberOfPatterns(self, m, n):
    # Write your code here
    graph = {
        1: {
            2: {
                3: {}
            },
            5: {
                9: {}
            },
            4: {
                7: {}
            },
            6: {},
            8: {}
        },
        2: {
            1: {},
            3: {},
            4: {},
            6: {},
            7: {},
            9: {},
            5: {
                8: {}
            }
        },
        3: {
            2: {
                1: {}
            },
            5: {
                7: {}
            },
            6: {
                9: {}
            },
            4: {},
            8: {}
        },
        4: {
            1: {},
            2: {},
            3: {},
            7: {},
            8: {},
            9: {},
            5: {
                6: {}
            }
        },
        5: {
            1: {},
            2: {},
            3: {},
            4: {},
            6: {},
            7: {},
            8: {},
            9: {}
        },
        6: {
            1: {},
            2: {},
            3: {},
            8: {},
            7: {},
            9: {},
            5: {
                4: {}
            }
        },
        7: {
            4: {
                1: {}
            },
            5: {
                3: {}
            },
            8: {
                9: {}
            },
            2: {},
            6: {}
        },
        8: {
            1: {},
            3: {},
            4: {},
            6: {},
            7: {},
            9: {},
            5: {
                2: {}
            }
        },
        9: {
            6: {
                3: {}
            },
            5: {
                1: {}
            },
            8: {
                7: {}
            },
            2: {},
            4: {}
        },
    }

    def recurse(path):
      if len(path) >= m:
        cnt[0] += 1
      if len(path) == n:
        return
      curr = path[-1]
      pks = set(path)
      d1 = set(graph[curr].keys())
      for k in graph[curr].keys():
        if k in pks:
          d1.update(graph[curr][k].keys())
      for k in d1.difference(pks):
        recurse(path + [k])

    cnt = [0]
    tcnt = 0
    recurse([1])
    tcnt += cnt[0] * 4
    cnt[0] = 0
    recurse([2])
    tcnt += cnt[0] * 4
    cnt[0] = 0
    recurse([5])
    tcnt += cnt[0]
    return tcnt


print(Solution().numberOfPatterns(8, 9))
