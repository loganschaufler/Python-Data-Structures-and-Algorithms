"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,1,2]
Output: [1,2]
"""

#Time: O(n)
#Space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = curr = head
        while curr.next:
        	if curr.val == curr.next.val:
        	    curr.next = curr.next.next
            else:
	            curr = curr.next
        return dummy