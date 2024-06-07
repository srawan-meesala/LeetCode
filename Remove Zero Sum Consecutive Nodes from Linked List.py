import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head):
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            print(seen)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next


# ln = ListNode(1)
# ln.next = ListNode(2)
# ln.next.next = ListNode(3)
# ln.next.next.next = ListNode(-3)
# ln.next.next.next.next = ListNode(4)

ln = ListNode(1)
ln.next = ListNode(2)
ln.next.next = ListNode(3)
ln.next.next.next = ListNode(-3)
ln.next.next.next.next = ListNode(-2)

sol = Solution()
k = sol.removeZeroSumSublists(ln)
print("  ")
while k.next:
    print(k.val)
    k = k.next
print(k.val)
