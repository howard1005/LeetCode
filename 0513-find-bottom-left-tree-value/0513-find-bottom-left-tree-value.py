# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        
        def dfs(node,h):
            d[h].append(node.val)
            if node.left:
                dfs(node.left,h+1)
            if node.right:
                dfs(node.right,h+1)
                
        dfs(root,0)
        
        return d[len(d)-1][0]