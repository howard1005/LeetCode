# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def dfs(node,isleft):
            if isleft and not node.left and not node.right:
                nonlocal ans
                ans += node.val
            if node.left:
                dfs(node.left,True)
            if node.right:
                dfs(node.right,False)
        dfs(root,False)
        return ans