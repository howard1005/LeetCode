# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        
        d = defaultdict(int)
        def dfs(node,level):
            d[level] += node.val
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
        dfs(root,1)
        
        return -max([(cum,-level) for level,cum in d.items()])[1]