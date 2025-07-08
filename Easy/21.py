# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        elif not list2:
            return list1
        head = None
        prev = None
        curr = None
        while list1 is not None and list2 is not None:
            curr = ListNode(val=None,next=None)
            if list1.val <= list2.val:
                curr.val = list1.val
                list1 = list1.next
            else: 
                curr.val = list2.val
                list2 = list2.next
            if not head:
                head = curr
            if prev:
                prev.next = curr
            prev = curr
            print('1 ',list1)
            print('2 ',list2)
            print('head ',head)
        if not list1:
            prev.next = list2
        elif not list2:
            prev.next = list1
        else:
            print('Unexpected error')
        return head
