# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            ret1 = ret2 = 0
            if node.left:
                ret1 = 1+dfs(node.left)
            if node.right:
                ret2 = 1+dfs(node.right)
            nonlocal ans
            ans = max(ans,ret1+ret2)
            return max(ret1,ret2)
        dfs(root)
        return ans