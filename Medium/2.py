# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        first_link = None
        prev_link = None
        use_as_last = None
        while l1.next is not None and l2.next is not None:
            if l1.next is None and l2.next is not None:
                new_val = l2.val + carry
                use_as_last = 'l2'
            elif l1.next is not None and l2.next is None:
                new_val = l1.val + carry
                use_as_last = 'l1'
            else:
                new_val = l1.val + l2.val + carry
            carry = 0
            if new_val >= 10:
                adjust = new_val%10
                carry =(new_val-adjust)/10
                new_val = adjust
            curr_link = ListNode(val=new_val,next=None)
            if first_link is None:
                first_link = curr_link
            if prev_link is not None:
                prev_link.next = curr_link

            prev_link = curr_link

            if l1.next is not None:
                l1 = l1.next
            if l2.next is not None:
                l2 = l2.next
            print(l1.next)
            print(l2.next)
            if l1.next is None and l2.next is None:
                break

        if use_as_last=='l1':
            curr_link = ListNode(val=l1.val,next=None)
        elif use_as_last=='l2':
            curr_link = ListNode(val=l2.val,next=None)
        prev_link.next = curr_link
        return first_link