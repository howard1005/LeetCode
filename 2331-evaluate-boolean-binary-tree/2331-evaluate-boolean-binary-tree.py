# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.val < 2:
                return True if node.val else False 
            if node.left:
                c1 = dfs(node.left)
            if node.right:
                c2 = dfs(node.right)
            return (c1 or c2) if node.val == 2 else (c1 and c2)
        return dfs(root)