from typing import List, Optional

# class TreeNode: (LeetCode provides this)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        post_i = len(postorder) - 1

        def build(l, r):
            nonlocal post_i
            if l > r:
                return None

            root_val = postorder[post_i]
            post_i -= 1
            root = TreeNode(root_val)

            m = idx[root_val]
            root.right = build(m + 1, r)
            root.left = build(l, m - 1)
            return root

        return build(0, len(inorder) - 1)