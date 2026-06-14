from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        st = []
        slow, fast = head, head
        l, r = None, None
        while fast != None:
            fast = fast.next.next
            r = slow.next
            slow.next = l
            l = slow
            slow = r
        ans = 0
        while r != None:
            ans = max(ans, r.val + l.val)
            r = r.next
            l = l.next
        return ans
        


# Time Complexity: O(n)
# Space Complexity: O(1)