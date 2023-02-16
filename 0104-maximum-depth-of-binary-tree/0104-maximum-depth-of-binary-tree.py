# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def dfs(node,dpt):
            nonlocal ans
            ans = max(ans,dpt)
            if node.left:
                dfs(node.left,dpt+1)
            if node.right:
                dfs(node.right,dpt+1)
        dfs(root,0)
        return ans+1