from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue=[]
        queue.append(root)
        while queue:
            node=queue.pop(0)
            if node.val==val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None
            
def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])  # Create the root node
    queue = [root]  # Use a queue to keep track of nodes
    i = 1  # Start with the second element in the list
    
    while queue and i < len(values):
        current = queue.pop(0)  # Get the current node
        
        # Add the left child if the value is not None
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Add the right child if the value is not None
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Function to print the tree in level-order format
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values for a cleaner output
    while result and result[-1] is None:
        result.pop()
    
    return result
input_values = input("Enter the level-order traversal of the tree (use 'null' for None, separated by commas):\n")

# Convert input to a list of integers and None
tree_values = [
    int(x) if x.strip().lower() != "null" else None 
    for x in input_values.split(",")
]
val=int(input("Enter search val for the binary search tree:\n"))
root=build_tree(tree_values)
sol=Solution()
output=sol.searchBST(root,val)
print(f"The sub-tree with root {val} in the tree: {tree_values} is: {tree_to_list(output)}")