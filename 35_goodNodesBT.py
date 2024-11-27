from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack=[]
        stack.append((root, root.val))
        good_nodes=0
        while len(stack)!=0:
            node, current_max=stack.pop()
            if node.val>=current_max:
                good_nodes+=1
            new_max=max(node.val,current_max)
            if node.right:
                stack.append((node.right,new_max))
            if node.left:
                stack.append((node.left, new_max))

        return good_nodes

# Helper function to build the tree from a list (level-order)
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

# Take input from the user
input_values = input("Enter the level-order traversal of the tree (use 'null' for None, separated by commas): ")

# Convert input to a list of integers and None
tree_values = [
    int(x) if x.strip().lower() != "null" else None 
    for x in input_values.split(",")
]

# Build the tree and calculate the maximum depth
root = build_tree(tree_values)
sol = Solution()
print(f"Number of good nodes in the tree {tree_values} is {sol.goodNodes(root)} ")            
            
