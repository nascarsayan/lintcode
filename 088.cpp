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
  pair<bool, bool> recurse(TreeNode *root, TreeNode *A, TreeNode *B,
                           TreeNode **lca) {
    bool Afound = false, Bfound = false;
    if (!root)
      return make_pair(false, false);
    if (*lca)
      return make_pair(true, true);
    if (root == A)
      Afound = true;
    if (root == B)
      Bfound = true;
    pair<bool, bool> found;
    found = recurse(root->left, A, B, lca);
    Afound |= found.first;
    Bfound |= found.second;
    if (Afound && Bfound) {
      if (!(*lca)) {
        *lca = root;
        return make_pair(true, true);
      }
    }
    found = recurse(root->right, A, B, lca);
    Afound |= found.first;
    Bfound |= found.second;
    if (Afound && Bfound) {
      if (!(*lca)) {
        *lca = root;
        return make_pair(true, true);
      }
    }
    return make_pair(Afound, Bfound);
  }

  /*
   * @param root: The root of the binary search tree.
   * @param A: A TreeNode in a Binary.
   * @param B: A TreeNode in a Binary.
   * @return: Return the least common ancestor(LCA) of the two nodes.
   */
  TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *A, TreeNode *B) {
    // write your code here
    TreeNode *lca = NULL;
    if (A == B)
      return A;
    if (A != NULL && B == NULL)
      return A;
    if (A == NULL && B != NULL)
      return B;
    recurse(root, A, B, &lca);
    return lca;
  }
};