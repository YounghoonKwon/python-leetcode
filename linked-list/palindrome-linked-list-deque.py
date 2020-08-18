# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        deq = Deque = collections.deque()
        if not head:
            return True        
        node = head
        while node is not None:
            deq.append(node.val)
            node = node.next
        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False
        return True
