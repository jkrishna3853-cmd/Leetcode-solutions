from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        pre_i = 0

        def build(l, r):
            nonlocal pre_i
            if l > r:
                return None

            root_val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(root_val)

            m = idx[root_val]
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(inorder) - 1)      
