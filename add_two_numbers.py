from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next = None):
         self.val = val
         self.next = next


class Solution:
    def getNum(self, linked_list: Optional[ListNode]) -> int:
        answer = ''

        while linked_list is not None:
            answer += str(linked_list.val)
            linked_list = linked_list.next

        return int(answer[::-1])

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.getNum(l1)
        n2 = self.getNum(l2)

        result = n1 + n2

        start_node = ListNode(val=result % 10)
        prev_node = start_node
        result //= 10

        while result != 0:
            next_node = ListNode(val=result % 10)
            prev_node.next = next_node

            result //= 10
            prev_node = next_node

        return start_node
