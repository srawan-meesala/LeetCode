class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head):
        if not head:
            return head
        t1, t2 = ListNode(0), head
        t1.next = head
        carry, extra = 0, ListNode(0)
        while t2.next:
            curr = t2.val*2
            if curr > 9:
                curr -= 10
                if t2 == head:
                    extra.val = 1
                t1.val += 1 
            t2.val = curr
            t1 = t1.next
            t2 = t2.next
        curr = t2.val*2
        if curr > 9:
            if t2 == head: extra = True
            curr -= 10
            carry += 1
        t2.val = curr
        t1.val += carry
        if extra.val == 0:
            return head
        else:
            extra.next = head
            return extra 
        
a = ListNode(1)
a.next = ListNode(8)
a.next.next = ListNode(9)

sol = Solution()
p = sol.doubleIt(a)
while p.next:
    print(p.val)
    p = p.next
print(p.val)