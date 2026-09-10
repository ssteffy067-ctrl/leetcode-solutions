# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        self.result = 0

        def traverse(node):

            # Empty subtree contributes 0 sum and 0 nodes
            if not node:
                return 0, 0

            # Get sum and count from both child subtrees
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            
            # Include current node in the subtree
            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count

            # Check if floor(average) equals current node's value
            if curr_sum // curr_count == node.val:
                self.result += 1

            # Pass this subtree's sum and count to its parent
            return curr_sum, curr_count

        traverse(root)

        return self.result
