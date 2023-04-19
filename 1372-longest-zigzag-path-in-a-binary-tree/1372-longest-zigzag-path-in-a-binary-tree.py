# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node,lr):
            nonlocal ans
            
            retl = [0,0]
            
            if node.left:
                retl[0] = dfs(node.left,0) + 1
            if node.right:
                retl[1] = dfs(node.right,1) + 1
            
            ans = max(ans, retl[0], retl[1])
            
            return retl[1] if lr == 0 else retl[0]
                
            
        dfs(root,-1)
            
        return ans