# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans = True
        
        l = []
        def dfs(node):
            if not node:
                l.append(None)
                return
            l.append(node.val)
            dfs(node.left)
            dfs(node.right)
        rl = []
        def rdfs(node):
            if not node:
                rl.append(None)
                return
            rl.append(node.val)
            rdfs(node.right)
            rdfs(node.left)
            
        
        dfs(root)
        rdfs(root)
        
        return l == rl