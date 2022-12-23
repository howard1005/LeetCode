# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            need = node.val-1
            if node.left:
                t = dfs(node.left)
                ans += abs(t)
                need += t
            if node.right:
                t = dfs(node.right)
                ans += abs(t)
                need += t
            return need
        dfs(root)

        return ans