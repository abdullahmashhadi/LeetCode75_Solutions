from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def twinSum(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #O(n) time, O(n) space
        # cur_node=head
        # length=0
        # arr=[]
        # while (cur_node):
        #     length+=1
        #     arr.append(cur_node.val)
        #     cur_node=cur_node.next
        # max_sum=-1
        # i=0
        # j=len(arr)-1
        # while(i<j):
        #     max_sum=max(arr[i]+arr[j],max_sum)
        #     i+=1
        #     j-=1
        # return max_sum
        
        #O(n) time, O(1) space
        fast=head
        slow=head
        prev=None
        max_val=-1
        while fast and fast.next:
            fast=fast.next.next
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        while(slow):
            max_val=max(max_val,slow.val+prev.val)
            prev=prev.next
            slow=slow.next
        return max_val
        
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
max_sum = sol.twinSum(head)
print(f"Maximum twin sum of the linked list is: {max_sum}")
        