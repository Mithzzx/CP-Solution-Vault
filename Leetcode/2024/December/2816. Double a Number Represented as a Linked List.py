# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        p = head
        while p:
            stack.append(head.val)
            p = p.next
        s = ''.join(stack)
        i = str(2 * int(s))
        p = head
        for j in i:
            if p:
                p.val = j
            else:
                p = ListNode(j)
            p = p.next

        return head
