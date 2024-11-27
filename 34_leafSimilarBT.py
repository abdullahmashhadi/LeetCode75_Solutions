from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_list1=[]
        leaf_list2=[]
        stack=[]
        stack.append(root1)
        while len(stack)!=0:
            node1=stack.pop()
            if not node1:
                continue
            if node1.left is None and node1.right is None:
                leaf_list1.append(node1.val)
            else:
                stack.append(node1.left)
                stack.append(node1.right)
        stack=[]
        stack.append(root2)
        while len(stack)!=0:
            node2=stack.pop()
            if not node2:
                continue
            if node2.left is None and node2.right is None:
                leaf_list2.append(node2.val)
            else:
                stack.append(node2.left)
                stack.append(node2.right)
        return leaf_list1==leaf_list2


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
input_values1 = input("Enter the level-order traversal of the 1st tree (use 'null' for None, separated by commas): ")
input_values2 = input("Enter the level-order traversal of the 2nd tree (use 'null' for None, separated by commas): ")

# Convert input to a list of integers and None
tree_values1 = [
    int(x) if x.strip().lower() != "null" else None 
    for x in input_values1.split(",")
]
tree_values2 = [
    int(x) if x.strip().lower() != "null" else None 
    for x in input_values2.split(",")
]

# Build the tree and calculate the maximum depth
root1 = build_tree(tree_values1)
root2 = build_tree(tree_values2)
sol = Solution()
output=sol.leafSimilar(root1,root2)
print(f"The trees: {tree_values1} and {tree_values2} are leaf similar? {output}")
            
        