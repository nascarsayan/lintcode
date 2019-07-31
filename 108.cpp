#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  /**
   * @param s: A string
   * @return: An integer
   */
  int minCut(string &s) {
    // write your code here
    int sz = s.size(), i, leng, st, ist, ifl, minv, mid;
    vector<vector<int>> dp;
    for (i = 0; i < sz; i++) {
      vector<int> row(sz, INT_MAX);
      dp.push_back(row);
      dp[i][i] = 0;
    }
    for (leng = 2; leng < sz + 1; leng++) {
      for (st = 0; st < sz - leng + 1; st++) {
        ist = st + 1;
        ifl = max(st + 1, st + leng - 2);
        if (dp[ist][ifl] == 0 and s[st] == s[st + leng - 1])
          dp[st][st + leng - 1] = 0;
        else {
          minv = INT_MAX;
          for (mid = st; mid < st + leng - 1; mid++)
            minv = min(minv, dp[st][mid] + 1 + dp[mid + 1][st + leng - 1]);
          dp[st][st + leng - 1] = minv;
        }
      }
    }
    return dp[0][sz - 1];
  }
};