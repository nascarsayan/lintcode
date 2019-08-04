#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  /*
   * @param s: A string
   * @param dict: A dictionary of words dict
   * @return: A boolean
   */
  vector<string> wordBreak(string &s, unordered_set<string> &dict) {
    // write your code here
    int i, j, k, l = s.length(), piece2;
    vector<vector<string>> dp(l + 1, vector<string>(0));
    vector<int> matched;
    // dp[l].push_back("");
    for (i = l - 1; i >= 0; i--) {
      piece2 = false;
      if (dict.find(s.substr(i)) != dict.end()) {
        piece2 = true;
        dp[i].push_back(s.substr(i));
      }

      for (j = 0; j < matched.size(); j++) {
        if (dict.find(s.substr(i, matched[j] - i)) != dict.end()) {
          piece2 = true;
          for (k = 0; k < dp[matched[j]].size(); k++)
            dp[i].push_back(s.substr(i, matched[j] - i) + ' ' +
                            dp[matched[j]][k]);
        }
      }
      if (piece2)
        matched.insert(matched.begin(), i);
    }
    return dp[0];
  }
};

int main() {
  unordered_set<string> dict;
  dict.insert("de");
  dict.insert("ding");
  dict.insert("co");
  dict.insert("code");
  dict.insert("lint");
  string s = "lintcode";
  Solution().wordBreak(s, dict);
  return 0;
}