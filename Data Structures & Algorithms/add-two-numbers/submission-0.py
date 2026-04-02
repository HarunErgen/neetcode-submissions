# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        curr = dummy
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            res = total % 10
            carry = total // 10

            curr.next = ListNode(res)
            curr = curr.next
            l1, l2 = l1.next, l2.next
        
        p = l1 or l2
        while p:
            total = p.val + carry
            res = total % 10
            carry = total // 10

            curr.next = ListNode(res)
            curr = curr.next
            p = p.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next


