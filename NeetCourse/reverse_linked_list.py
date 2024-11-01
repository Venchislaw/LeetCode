"""ITERATIVE SOLUTION: """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next  # tmp variable
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

"""RECURSIVE SOLUTION:"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return new_head
