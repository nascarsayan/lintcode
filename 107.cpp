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
    vector<int> matched;
    dp[l] = true;
    for (i = l - 1; i >= 0; i--) {
      if (dict.find(s.substr(i)) != dict.end()) {
        matched.insert(matched.begin(), i);
        dp[i] = true;
        continue;
      }
        for (j = 0; j < matched.size(); j++) {
          if (dict.find(s.substr(i, matched[j] - i)) != dict.end()) {
            matched.insert(matched.begin(), i);
            dp[i] = true;
            break;
          }
        }
    }
    return dp[0];
  }
};

int main() {
  unordered_set<string> dict;
  dict.insert("a");
  dict.insert("b");
  dict.insert("c");
  dict.insert("d");
  dict.insert("e");
  dict.insert("f");
  dict.insert("g");
  string s = "abcdeeef";
  if (Solution().wordBreak(s, dict)) cout << "True\n";
  else cout << "False\n";
}