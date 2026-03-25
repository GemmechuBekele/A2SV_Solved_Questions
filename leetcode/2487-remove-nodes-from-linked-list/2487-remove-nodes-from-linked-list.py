# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def modify(node):
            if node is None:
                return None
            node.next = modify(node.next)
            if node.next and node.next.val > node.val:
                return node.next
            return node
        return modify(head)
        