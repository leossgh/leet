# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        saved_head = head
        node_nr = 1
        while True:
            if head.next == None:
                break
            node_nr += 1
            head = head.next
            if node_nr%2 == 0:
                saved_head = saved_head.next
        return saved_head

class PythonSolution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        saved_head = head
        node_nr = 1
        while True:
            if head.next == None:
                break
            node_nr += 1
            head = head.next
            if node_nr%2 == 0:
                saved_head = saved_head.next
        return saved_head