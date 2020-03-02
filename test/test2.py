# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        new_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_node


l5 = ListNode(5)
l4 = ListNode(4)
l4.next = l5
l3 = ListNode(3)
l3.next = l4
l2 = ListNode(2)
l2.next = l3
l1 = ListNode(1)
l1.next = l2
# print(l1)
sl = Solution()
r = sl.reverseList(l1)
