# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ''
        def dfs(node):
            nonlocal ans
            ans += str(node.val)
            if node.left:
                ans += '('
                dfs(node.left)
                ans += ')'
            if node.right:
                if not node.left:
                    ans += '()'
                ans += '('
                dfs(node.right)
                ans += ')'
        dfs(root)
        return ans