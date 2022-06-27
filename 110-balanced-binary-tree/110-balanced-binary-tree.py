# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        return abs(self.height(root.left)- self.height(root.right)) < 2 and self.isBalanced(root.right) and self.isBalanced(root.left)
     
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    