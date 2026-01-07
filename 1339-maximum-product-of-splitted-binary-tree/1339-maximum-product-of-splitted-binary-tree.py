# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        ans = 0
        ss = []
        def dfs(node):
            ret = node.val
            if node.left:
                ret += dfs(node.left)
            if node.right:
                ret += dfs(node.right)
            ss.append(ret)
            return ret
        tot = dfs(root)
        print(ss)
        for v in ss[:-1]:
            ans = max(ans,(tot-v)*v)
        return ans % 1000000007