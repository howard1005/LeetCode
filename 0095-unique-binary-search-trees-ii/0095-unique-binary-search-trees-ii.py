# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(s,e):
            if s > e:
                return [None]
            ret = []
            for i in range(s,e+1):
                lefts = dfs(s,i-1)
                rights = dfs(i+1,e)
                for left in lefts:
                    for right in rights:
                        ret.append(TreeNode(i,left,right))
            return ret
                        
        return dfs(1,n)