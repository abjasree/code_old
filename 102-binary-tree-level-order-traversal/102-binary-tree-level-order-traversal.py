# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        q = []
        
        result = []
        q.append(root)
        while len(q) > 0:
            level = []
            q_l = len(q)
            for i in range(q_l):
                node = q.pop(0)
                level.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            result.append(level)
                
        return result
            
        
        