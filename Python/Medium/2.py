# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MemorySolution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        first_link = None
        prev_link = None
        use_l1_last = None
        
        while l1 != None or l2 != None:
            if l1 == None and l2 != None:
                new_val = l2.val + carry
                use_l1_last = False
            elif l1 != None and l2 == None:
                new_val = l1.val + carry
                use_l1_last = True
            else:
                new_val = l1.val + l2.val + carry

            carry = 0

            if new_val >= 10:
                adjust = new_val%10
                carry =(new_val-adjust)/10
                new_val = adjust
                
            curr_link = ListNode(val=new_val,next=None)
            if first_link == None:
                first_link = curr_link
            if prev_link != None:
                prev_link.next = curr_link

            prev_link = curr_link

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry:
            curr_link = ListNode(val=carry,next=None)
            prev_link.next = curr_link
        return first_link
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class PythonMemorySolution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        first_link = None
        prev_link = None
        
        while l1 != None or l2 != None:
            if l1 == None and l2 != None:
                new_val = l2.val + carry
                use_l1_last = False
            elif l1 != None and l2 == None:
                new_val = l1.val + carry
                use_l1_last = True
            else:
                new_val = l1.val + l2.val + carry

            carry = 0

            if new_val >= 10:
                adjust = new_val%10
                carry =(new_val-adjust)/10
                new_val = adjust
                
            curr_link = Solution.ListNode(val=new_val,next=None)
            if first_link == None:
                first_link = curr_link
            if prev_link != None:
                prev_link.next = curr_link

            prev_link = curr_link

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry:
            curr_link = Solution.ListNode(val=carry,next=None)
            prev_link.next = curr_link
        return first_link