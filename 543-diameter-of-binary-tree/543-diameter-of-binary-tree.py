# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    def dfs(self, root):
        if root == None:
            return 0
        left_dia = self.dfs(root.left)
        right_dia = self.dfs(root.right)
        self.diameter = max(self.diameter, left_dia + right_dia)
        return max(left_dia, right_dia)+1