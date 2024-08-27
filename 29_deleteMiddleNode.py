import math
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if not head or not head.next:
            return None
        length=0
        cur_node=head
        while cur_node!=None:
            length+=1
            cur_node=cur_node.next
        middle=math.floor(length/2)
        cur_idx=0
        cur_node=head
        while(cur_idx<middle-1):
            cur_node=cur_node.next
            cur_idx+=1
        cur_node.next=cur_node.next.next
        return head

def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    elems = []
    current = head
    while current:
        elems.append(current.val)
        current = current.next
    print(elems)

elements = list(map(int, input("Enter elements of your linked list (space-separated): ").split()))
head = create_linked_list(elements)
sol = Solution()
new_head = sol.deleteMiddle(head)
print("Linked list after deleting middle node:")
print_linked_list(new_head)