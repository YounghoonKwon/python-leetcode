class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev #assign next and prev
            node, prev = next, node #move pointer of next and prev
        return prev
