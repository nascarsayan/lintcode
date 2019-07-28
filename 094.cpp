#include <bits/stdc++.h>
using namespace std;
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class TreeNode {
public:
  int val;
  TreeNode *left, *right;
  TreeNode(int val) {
    this->val = val;
    this->left = this->right = NULL;
  }
};

class Solution {
public:
  /**
   * @param root: The root of binary tree.
   * @return: An integer
   */
  int recurse(TreeNode *root, int *maxsum) {
    *maxsum = max(*maxsum, root->val);
    if (!root->left && !root->right) {
      return root->val;
    }
    int lsum = INT_MIN, rsum = INT_MIN;
    if (root->left) {
      lsum = recurse(root->left, maxsum);
      *maxsum = max(*maxsum, lsum + root->val);
    }
    if (root->right) {
      rsum = recurse(root->right, maxsum);
      *maxsum = max(*maxsum, rsum + root->val);
    }
    if (lsum != INT_MIN && rsum != INT_MIN) {
      *maxsum = max(*maxsum, lsum + rsum + root->val);
    }
    int maxchsum = max(lsum, rsum);
    if (maxchsum <= 0)
      return root->val;
    return root->val + maxchsum;
  }

  int maxPathSum(TreeNode *root) {
    // write your code here
    if (!root)
      return INT_MIN;
    int maxsum = INT_MIN;
    recurse(root, &maxsum);
    return maxsum;
  }
};