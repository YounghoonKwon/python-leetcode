class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a= self.toList(self.reverseList(l1))
        b= self.toList(self.reverseList(l2))
        sum = (int(''.join(str(e) for e in a))) + (int (''.join(map(str, b))))
        return (self.strToListNode((str(sum)[::-1])))
        
    def reverseList(self, head:ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
        
    def toList(self, node:ListNode) -> List:
        list : List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    def strToListNode(self, string:str) -> ListNode:
        head = node = ListNode(0)
        for char in string:
            node.next = ListNode(char)
            node = node.next
        return head.next
