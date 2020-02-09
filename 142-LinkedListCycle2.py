class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        slow = head
        fast = slow
        while slow != None and fast !=None :
            slow = slow.next
            fast = fast.next
            if fast != None: fast = fast.next
            if slow == fast: break
            
        if slow == None and fast == None: return None
        # print(slow.val)
        slow = head
        while slow!=fast:
            slow = slow.next
            if fast!=None: fast = fast.next
        
        return slow