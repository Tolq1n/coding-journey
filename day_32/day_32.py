#206. Reverse Linked List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        reversed_list = None
        current = head

        while current:
            next_node = current.next
            current.next = reversed_list
            reversed_list = current
            current = next_node

        return reversed_list

#83. Remove Duplicates from Sorted List
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None or head.next is None:
#             return head
#         org = head.next
#         while org:
#             try:
#                 if org.val == org.next.val:
#                     org.next = org.next.next
#                     continue
#             except:
#                 break
#             org = org.next

#         if head.val == head.next.val:
#             head = head.next
#         return head
