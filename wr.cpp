#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  /**
   * @param S: a string
   * @param words: a list of strings
   * @return: return a integer
   */
  int expressiveWords(string &S, vector<string> &words) {
    int n = words.size();
    int sol = 0;
    for (int i = 0; i < n; i++) {
      if (words[i].length() > S.length()) {
        continue;
      } else {
        int flag = 1;
        int index = 0;
        int j;
        for (j = 0; j < words[i].length();) {
          char x = words[i][j];
          int count1 = 0;
          int count2 = 0;
          while (S[index] == x && index < S.length()) {
            index++;
            count1++;
          }
          while (words[i][j] == x) {
            j++;
            count2++;
          }
          if (count2 == count1) {
            continue;
          } else if (count2 < count1 && count1 >= 3) {
            continue;
          } else {
            flag = 0;
            break;
          }
        }
        if (flag && j == words[i].length())
          sol++;
      }
    }
    return sol;
  }
};