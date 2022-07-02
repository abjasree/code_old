# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)
        
        
    def helper(self, node):
        if node == None:
            return 0
        if node.right == None and node.left == None:
            return 1
        left = self.helper(node.left)
        right = self.helper(node.right)
        return max(left, right) + 1
        
        