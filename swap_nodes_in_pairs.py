from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        next_node = head.next
        if next_node is None:
            return head

        next_node.val, head.val = head.val, next_node.val

        self.swapPairs(next_node.next)
        return head
