# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = inf
        
        l = []
        def dfs(node):
            l.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        l.sort()
        
        for i in range(len(l)-1):
            ans = min(ans,abs(l[i]-l[i+1]))
            
        return ans
        