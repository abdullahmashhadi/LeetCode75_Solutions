from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur_node=head
        prev_node=None
        while(cur_node):
            nxt=cur_node.next
            cur_node.next=prev_node
            prev_node=cur_node
            cur_node=nxt
        return prev_node
        
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
new_head = sol.reverseList(head)
print("Linked list reversed:")
print_linked_list(new_head)
        