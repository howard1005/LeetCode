# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node,h):
            if h == depth-1:
                node.left = TreeNode(val,node.left,None)
                node.right = TreeNode(val,None,node.right)
            else:
                if node.left:
                    dfs(node.left,h+1)
                if node.right:
                    dfs(node.right,h+1)
        if depth == 1:
            root = TreeNode(val,root,None)
        else:   
            dfs(root,1)
        return root