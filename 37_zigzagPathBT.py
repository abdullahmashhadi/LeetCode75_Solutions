from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.zigzag=0
        def dfs(node,direction,length):
            if not node:
                return
            self.zigzag=max(self.zigzag,length)
            if direction=='left':
                dfs(node.left,'right',length+1)
                dfs(node.right,'left',1)
            else:
                dfs(node.right,'left',length+1)
                dfs(node.left,'right',1)
        dfs(root,'left',0)
        dfs(root,'right',0)
        return self.zigzag
    
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
input_values = input("Enter the level-order traversal of the tree (use 'null' for None, separated by commas): ")

# Convert input to a list of integers and None
tree_values = [
    int(x) if x.strip().lower() != "null" else None 
    for x in input_values.split(",")
]

root=build_tree(tree_values)
sol=Solution()
output=sol.longestZigZag(root)
print(f"The longest zigzag path in the tree: {tree_values} is: {output}")