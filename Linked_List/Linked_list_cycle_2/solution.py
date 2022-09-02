class Solution:
    def detectCycle(self, head:ListNode)->ListNode:
        if not head:
            return
        slow,fast = head,head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

            if not fast.next or not fast.next.next:
                return

            slow2 = head

            while slow.next:
                if slow == slow2:
                    return slow
                slow = slow.next
                slow2 = slow2.next
            return
