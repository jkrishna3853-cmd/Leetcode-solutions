class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        self.current = head

        def build_tree(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            
            mid = (start + end) // 2
            
            left_child = build_tree(start, mid - 1)

            root = TreeNode(self.current.val)
            root.left = left_child
            
            self.current = self.current.next
            
            root.right = build_tree(mid + 1, end)
            
            return root
        
        return build_tree(0, length - 1)