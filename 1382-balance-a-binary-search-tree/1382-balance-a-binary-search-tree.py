# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        l = []

        def dfs(node):
            l.append(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)

        l.sort(key=lambda x: x.val)

        def make(lo,hi):
            if lo>hi or lo<0 or hi>=len(l):
                return None
            i = (lo+hi)//2
            node = l[i]
            node.left = make(lo,i-1)
            node.right = make(i+1,hi)
            return node

        return make(0,len(l)-1)