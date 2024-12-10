class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = head.next
        x = []
        while p:
            x.append(p)
            p = head.next
        p = head
        while len(x) > 0:
            p.next = x.pop(-1)
            p.next.next = x.pop(0)
            p = p.next.next
            
        print("hello ")
            