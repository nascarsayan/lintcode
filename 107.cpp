#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  /*
   * @param s: A string
   * @param dict: A dictionary of words dict
   * @return: A boolean
   */
  bool wordBreak(string &s, unordered_set<string> &dict) {
    // write your code here
    int i, j, l = s.length();
    vector<bool> dp(l + 1, false);
    dp[l] = true;
    for (i = l - 1; i >= 0; i--) {
      for (j = i; j < l; j++) {
        if (dict.find(s.substr(i, j - i + 1)) != dict.end() && dp[j + 1]) {
          dp[i] = true;
          continue;
        }
      }
    }
    return dp[0];
  }
};