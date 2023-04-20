# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = defaultdict(list)
        def dfs(node,i,depth):
            d[depth].append(i)
            if node.left:
                dfs(node.left,i*2-1,depth+1)
            if node.right:
                dfs(node.right,i*2,depth+1)
        dfs(root,1,1)
        ans = 0
        for l in d.values():
            ans = max(ans,l[-1]-l[0]+1)
        return ans