// https://www.lintcode.com/problem/first-position-of-target/

#include <vector>
using namespace std;
class Solution {
public:
  /**
   * @param nums: The integer array.
   * @param target: Target to find.
   * @return: The first position of target. Position starts from 0.
   */
  int binarySearch(vector<int> &nums, int target) {
    // write your code here'
    int idx = -1, l = 0, h = nums.size() - 1, m;
    while (l <= h) {
      m = (l + h) / 2;
      if (nums.at(m) == target) {
        idx = m;
        break;
      }
      else if (nums.at(m) > target) {
        h = m - 1;
      } else {
        l = m + 1;
      }
    }
    if (idx == -1)
      return idx;
    while (idx > 0 && nums[idx - 1] == target)
      idx --;
    return idx;
  }
};