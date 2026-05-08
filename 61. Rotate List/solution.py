# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: 
            return head
        tail = head
        n = 1
        while tail.next:
            n += 1
            tail = tail.next
        k = k % n
        if k==0:
            return head
        pos = 1
        cur = head
        while pos<n-k:
            cur = cur.next
            pos += 1
        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead

        