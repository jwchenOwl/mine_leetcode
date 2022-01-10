# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_num = 0
        l = ListNode()
        l3 = l
        while True:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            l3_val = a + b + carry_num
            carry_num = l3_val // 10
            l3.val = l3_val
            l3.next = ListNode()
            if not l1 and not l2:
                return l
