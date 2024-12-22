# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        stack = []
        while p:
            stack.append(p.val)
            p = p.next
        stack.reverse()
        lp, rp = 0, 1
        while rp < len(stack):
            if stack[rp] < stack[lp]:
                stack.pop(rp)
            else:
                lp += 1
                rp += 1
