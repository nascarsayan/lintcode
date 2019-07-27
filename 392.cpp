#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
  /**
   * @param A: An array of non-negative integers
   * @return: The maximum amount of money you can rob tonight
   */
  long long houseRobber(vector<int> &A) {
    // write your code here
    int len = A.size(), i;
    if (len == 0)
      return 0;
    if (len < 3)
      return max(A[0], A[1]);
    vector<long long> maxrob(len, 0);
    maxrob[0] = A[0];
    maxrob[1] = max(A[0], A[1]);
    maxrob[2] = max(A[0] + A[2], A[1]);
    if (len == 3)
      return maxrob[2];
    for (i = 3; i < len; i++) {
      maxrob[i] = max(maxrob[i - 2], maxrob[i - 3]) + A[i];
    }
    return max(maxrob[len - 1], maxrob[len - 2]);
  }
};

int main() {
  vector<int> A{3, 8, 4};
  cout << Solution().houseRobber(A);
}