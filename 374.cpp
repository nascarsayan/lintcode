#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  /**
   * @param matrix: a matrix of m x n elements
   * @return: an integer list
   */
  vector<int> spiralOrder(vector<vector<int>> &matrix) {
    // write your code here
    int nr, nc, dep, i, j;
    nr = matrix.size();
    vector<int> spiro;
    if (nr == 0)
      return spiro;
    nc = matrix[0].size();
    if (nc == 0)
      return spiro;
    dep = 0;
    for (dep = 0; dep < (min(nr, nc) + 1) / 2; dep++) {
      for (j = dep; j < nc - dep; j++)
        spiro.push_back(matrix[dep][j]);
      for (i = dep + 1; i < nr - dep; i++)
        spiro.push_back(matrix[i][nc - 1 - dep]);
      if (nr - 1 - dep != dep) {
        for (j = nc - 2 - dep; j >= dep; j--)
          spiro.push_back(matrix[nr - 1 - dep][j]);
      }
      if (nc - 1 - dep != dep) {
        for (i = nr - 2 - dep; i > dep; i--)
          spiro.push_back(matrix[i][dep]);
      }
    }
    return spiro;
  }
};

int main() {
  vector<int> c1{1, 2, 3}, c2{5, 6, 7}, c3{9, 10, 11}, c4{12, 13, 14};
  vector<vector<int>> mat{c1, c2, c3, c4};
  for (auto x : Solution().spiralOrder(mat))
    cout << x << ' ';
  cout << '\n';
  return 0;
}