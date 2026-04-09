# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head

#         # find the middle of the list
#         step1_move = head
#         step2_move = head.next

#         while step2_move and step2_move.next:
#             step1_move = step1_move.next
#             step2_move = step2_move.next.next

#         # Split list (Cut the list into two halves)
#         mid = step1_move.next
#         step1_move.next = None

#         # Sort both halves
#         left = self.sortList(head)
#         right = self.sortList(mid)

#         #  Merge sorted halves
#         return self.merge(left, right)

#     def merge(self, left, right):
#         fake_start = ListNode(0)
#         tail = fake_start

#         while left and right:
#             if left.val < right.val:
#                 tail.next = left
#                 left= left.next
#             else:
#                 tail.next = right
#                 right = right.next
#             tail = tail.next

#         # Attach remaining nodes
#         if left:
#             tail.next = left
#         if right:
#             tail.next = right

#         return fake_start.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        mid = self.findMid(head)
        right = mid.next
        mid.next = None         

        left_sorted  = self.sortList(head)
        right_sorted = self.sortList(right)

        return self.merge(left_sorted, right_sorted)

    def findMid(self, head):
        one_step_move = head
        two_step_move = head.next       

        while two_step_move and two_step_move.next:
            one_step_move = one_step_move.next
            two_step_move = two_step_move.next.next

        return one_step_move            

    def merge(self, left, right):
        fake_start = ListNode(0)     
        current = fake_start

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        current.next = left if left else right

        return fake_start.next  
      