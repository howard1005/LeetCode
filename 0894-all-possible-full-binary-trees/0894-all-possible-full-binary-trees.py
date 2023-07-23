# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def dfs(n):
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode()]
            ret = []
            for i in range(1,n,2):
                ll = dfs(i)
                rl = dfs(n - i - 1)
                for ln in ll:
                    for rn in rl:
                        ret.append(TreeNode(0,ln,rn))
            return ret
        
        return dfs(n)