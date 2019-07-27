#include <climits>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  /**
   * @param nums: An array of integers
   * @return: An integer
   */
  int maxProduct(vector<int> &nums) {
    // write your code here
    int fstneg = 1, fstidx = -1, currp = 1, inum, maxp = INT_MIN,
        len = nums.size(), nexp;
    if (len == 0)
      return INT_MIN;
    if (len == 1)
      return nums[0];
    for (inum = 0; inum < len; inum++) {
      nexp = currp * nums[inum];
      maxp = max(maxp, nexp);
      if (nexp != 0) {
        if (nexp < 0 && fstneg > -1) {
          fstneg = nexp;
          fstidx = inum;
        }
        currp = nexp;
      } else {
        if (currp < 0 && fstidx != inum) {
          currp /= fstneg;
        }
        maxp = max(maxp, currp);
        currp = 1;
        fstneg = 1;
        fstidx = -1;
      }
    }
    if (currp < 0 && fstidx != currp) {
      maxp = max(maxp, currp / fstneg);
    }
    return maxp;
  }
};

int main() {
  vector<int> nums{2, 3, -2, 0, -4, -2, -5};
  cout << Solution().maxProduct(nums);
}