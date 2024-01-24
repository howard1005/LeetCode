# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:        
        ans = 0
        
        lc = [0 for _ in range(10)]
        def dfs(node):
            nonlocal ans
            lc[node.val] += 1
            flag = True
            if node.left:
                flag = False
                dfs(node.left)
            if node.right:
                flag = False
                dfs(node.right)
            if flag:
                oc = 0
                for c in lc:
                    if c % 2 == 1:
                        oc += 1
                if oc <= 1:
                    ans += 1
            lc[node.val] -= 1
        dfs(root)
        
        return ans