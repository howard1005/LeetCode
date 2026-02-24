# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, cum):
            cum = 2*cum + node.val
            if not node.left and not node.right:
                nonlocal ans
                ans += cum
            else:
                if node.left:
                    dfs(node.left, cum)
                if node.right:
                    dfs(node.right, cum)
        dfs(root,0)
        return ans