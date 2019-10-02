#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  /**
   * @param n: an integer
   * @return: 1 - n in lexicographical order
   */
  void recurse(vector<int> &arr, int n, int m) {
    if (m > n)
      return;
    arr.push_back(m);
    for (int i = 0; i < 10; i++)
      recurse(arr, n, m * 10 + i);
  }

  vector<int> lexicalOrder(int n) {
    // write your code here
    vector<int> res;
    for (int i = 1; i < 10; i++)
      recurse(res, n, i);
    return res;
  }
};