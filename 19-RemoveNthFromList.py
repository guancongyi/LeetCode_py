# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = ListNode(0)
        slow = start
        slow.next = head
        fast = slow
        

        count = 0
        while count != n+1:
            fast = fast.next
            count+=1
            
        # print(fast.val, slow.val)
        while fast != None:
            slow = slow.next
            fast = fast.next
        print(slow.val)
        
        if slow.next != None: slow.next = slow.next.next
        return start.next
        