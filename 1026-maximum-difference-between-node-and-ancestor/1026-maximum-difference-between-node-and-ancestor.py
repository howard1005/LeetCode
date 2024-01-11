# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def dfs(node,mn,mx):
            nonlocal ans
            ans = max([ans,node.val-mn,mx-node.val])
            if node.left:
                dfs(node.left,min(mn,node.val),max(mx,node.val))
            if node.right:
                dfs(node.right,min(mn,node.val),max(mx,node.val))
        dfs(root,float('inf'),0)
        return ans