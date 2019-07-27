#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  /**
   * @param heights: a vector of integers
   * @return: an integer
   */
  int maxArea(vector<int> &heights) {
    // write your code here
    int len = heights.size();
    if (len < 2)
      return 0;
    int st = 0, fl = len - 1, area;
    int maxarea = min(heights[st], heights[fl]) * (fl - st);
    while (st < fl) {
      area = min(heights[st], heights[fl]) * (fl - st);
      if (area > maxarea) {
        maxarea = area;
      }
      if (heights[st] < heights[fl])
        st++;
      else
        fl--;
    }
    return maxarea;
  }
};

int main() {
  vector<int> heights{1, 3, 2};
  cout << Solution().maxArea(heights);
}