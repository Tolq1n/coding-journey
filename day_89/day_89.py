#1290. Convert Binary Number in a Linked List to Integer

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans = 0
        while head:
            ans = 2*ans + head.val
            head = head.next
        return ans