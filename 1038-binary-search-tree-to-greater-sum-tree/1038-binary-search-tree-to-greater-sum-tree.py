# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def dfs(node,cum):
            i = node.val
            if node.right:
                cum = dfs(node.right,cum)
            cum += node.val
            node.val = cum
            if node.left:
                cum = dfs(node.left,cum)
            return cum

        dfs(root,0)

        return root


            
        