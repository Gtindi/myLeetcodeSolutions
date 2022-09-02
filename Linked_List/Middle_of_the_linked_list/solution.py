"""
Time complexity = O(n)
Space complexity = O(1)
"""
class Solution:
    def middleNode(self, head:Optional[ListNode])->Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
