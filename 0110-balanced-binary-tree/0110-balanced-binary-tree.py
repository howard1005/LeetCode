# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        ans = True
        
        def dfs(node):
            nonlocal ans
            lh,rh = 0,0
            if ans and node.left:
                lh = dfs(node.left)
            if ans and node.right:
                rh = dfs(node.right)
            if ans and abs(lh-rh) > 1:
                ans = False
            return max(lh,rh)+1
        dfs(root)
        
        return ans