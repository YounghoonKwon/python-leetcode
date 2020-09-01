class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        return root
        
