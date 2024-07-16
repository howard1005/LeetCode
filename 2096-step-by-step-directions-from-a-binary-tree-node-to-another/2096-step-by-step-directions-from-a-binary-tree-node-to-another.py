# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        sp,dp = None,None
        
        def dfs(node,pl):
            nonlocal sp,dp
            if node.val == startValue:
                sp = ''.join(pl)
            if node.val == destValue:
                dp = ''.join(pl)
            if node.left:
                pl.append('L')
                dfs(node.left,pl)
                pl.pop()
            if node.right:
                pl.append('R')
                dfs(node.right,pl)
                pl.pop()

        dfs(root,[])

        # print(sp,dp)

        i = 0
        while i<min(len(sp),len(dp)):
            if sp[i] != dp[i]:
                break
            i += 1

        return 'U'*(len(sp)-i) + dp[i:]

        


