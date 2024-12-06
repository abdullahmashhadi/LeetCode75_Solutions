from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum=float('-inf')
        queue=[]
        queue.append(root)
        level=0
        maxLevel=0
        while queue:
            level+=1
            length=len(queue)
            levelSum=0
            for i in range(length):
                node=queue.pop(0)
                levelSum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if (maxSum<levelSum):
                maxLevel=level
            maxSum=max(maxSum,levelSum)
        return maxLevel

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
output=sol.maxLevelSum(root)
print(f"The level (1-indexed) with maximum sum in the tree: {tree_values} is: {output}")