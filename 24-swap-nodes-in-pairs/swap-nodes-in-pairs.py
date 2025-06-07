# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head 
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            if node.next.next:
                node = node.next.next
            else:
                break
        return head
