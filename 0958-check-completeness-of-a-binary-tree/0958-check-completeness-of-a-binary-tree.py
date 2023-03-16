# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        d = {}
        
        def dfs(node,n):
            d[n] = 1
            if node.left:
                dfs(node.left,n*2)
            if node.right:
                dfs(node.right,n*2+1)
        dfs(root,1)
        
        
        return max(d.keys()) == len(d)
        
        
    