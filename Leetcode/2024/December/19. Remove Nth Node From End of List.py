# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:

        x=[]
        itr = head
        while itr:
            x.append(itr.val)
            itr = itr.next

        x.pop(-n)
        return x


S = Solution()
print(S.removeNthFromEnd(head=[1, 2, 3, 4, 5], n=2))
