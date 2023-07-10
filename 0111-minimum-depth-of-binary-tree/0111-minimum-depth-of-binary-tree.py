# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = inf
        
        def dfs(node,h):
            nonlocal ans
            if node.left:
                dfs(node.left,h+1)
            if node.right:
                dfs(node.right,h+1)
            if not node.left and not node.right:
                ans = min(ans,h)
        dfs(root,1)
        
        return ans
            