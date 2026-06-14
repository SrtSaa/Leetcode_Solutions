from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        st = []
        while fast != None:
            st.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        ans = 0
        while slow != None:
            ans = max(ans, slow.val + st.pop())
            slow = slow.next
        return ans
        


# Time Complexity: O(n)
# Space Complexity: O(n/2)