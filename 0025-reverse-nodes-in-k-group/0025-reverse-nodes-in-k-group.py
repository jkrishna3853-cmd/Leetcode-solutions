# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prevGroupEnd = dummy
        
        while True:

            cursor = prevGroupEnd
            for _ in range(k):
                cursor = cursor.next
                if not cursor:
                    return dummy.next
            
            groupStart = prevGroupEnd.next
            nextGroupStart = cursor.next
            
            prev = nextGroupStart
            curr = groupStart
            
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            prevGroupEnd.next = prev
            prevGroupEnd = groupStart