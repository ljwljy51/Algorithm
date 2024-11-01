# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 두 개의 포인터 정의
        # prev 포인터 초기화
        prev = None
        # curr 포인터 초기화
        curr = head

        while curr:  # curr이 None에 도달할 때까지
            next = curr.next
            curr.next = prev

            # reverse
            prev = curr
            curr = next
        return prev
