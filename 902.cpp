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
#include <bits/stdc++.h>
using namespace std;
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
   * @param root: the given BST
   * @param k: the given k
   * @return: the kth smallest element in BST
   */
  int getLexVal(TreeNode *root) {
    if (!root->left)
      return root->val;
    return getLexVal(root->left);
  }

  void inorder(TreeNode *root, int lexVal, int k, int &curr, int &kth) {
    if (!root)
      return;
    this->inorder(root->left, lexVal, k, curr, kth);
    if (curr > 0)
      curr++;
    if (root->val == lexVal)
      curr = 1;
    if (curr == k) {
      kth = root->val;
      return;
    }
    this->inorder(root->right, lexVal, k, curr, kth);
  }

  int kthSmallest(TreeNode *root, int k) {
    // write your code here
    int lexVal = this->getLexVal(root);
    int kth = -1, curr = -1;
    this->inorder(root, lexVal, k, curr, kth);
    return kth;
  }
};

int main() {
  Solution s = Solution();
  vector<TreeNode> vt;
  TreeNode *root;
  int vals[] = {5, 3, 6, 2, 4, 1};
  for (int i = 0; i < 6; i++) {
    TreeNode temp(vals[i]);
    vt.push_back(temp);
  }
  root = &vt[0];
  (&vt[0])->left = &vt[1];
  (&vt[0])->right = &vt[2];
  (&vt[1])->left = &vt[3];
  (&vt[1])->right = &vt[4];
  (&vt[3])->right = &vt[5];

  cout << s.kthSmallest(root, 3) << '\n';
  return 0;
}