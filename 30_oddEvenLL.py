from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even=head
        odd=head.next
        odd_head=odd
        while(even.next and odd.next):
            even.next=odd.next
            even=even.next
            odd.next=even.next
            odd=odd.next
        even.next=odd_head
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
new_head = sol.oddEvenList(head)
print("Linked list with odd nodes first:")
print_linked_list(new_head)
        