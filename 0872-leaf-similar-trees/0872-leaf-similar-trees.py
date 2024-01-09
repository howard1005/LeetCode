# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,l):
            if not node.left and not node.right:
                l.append(node.val)
                return
            if node.left:
                dfs(node.left,l)
            if node.right:
                dfs(node.right,l)
        l1,l2 = [],[]
        dfs(root1,l1)
        dfs(root2,l2)
        return l1==l2
            