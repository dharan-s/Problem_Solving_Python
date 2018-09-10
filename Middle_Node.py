#Finding middle of linked list.
#Given a non-empty, singly linked list with head node head, return a middle node of linked list.

#If there are two middle nodes, return the second middle node.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        total_nodes = 0
        while p is not None:
            total_nodes += 1
            p = p.next 
            
        middle = int(total_nodes/2)
        
        p = head
        current_node=0
        while p.next is not None:
            if current_node == middle:
                break
            head = p.next
            p = p.next
            current_node += 1 
        
        return head