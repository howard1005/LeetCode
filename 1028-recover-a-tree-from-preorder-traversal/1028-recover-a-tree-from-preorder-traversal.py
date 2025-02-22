# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nl = []

        depth = 0
        n = 0
        for c in traversal:
            if c == '-':
                if n:
                    nl.append((n,depth))
                    n = 0
                    depth = 0
                depth += 1
            else:
                n = n*10+int(c)
        if n:
            nl.append((n,depth))

        def dfs(l):
            v,dep = l[0]

            node = TreeNode(v)

            if len(l)>1:
                lv,ldep = l[1]
                i = 2
                while i < len(l):
                    if l[i][1] == ldep:
                        break
                    i += 1
                if i == len(l):
                    node.left = dfs(l[1:])
                else:
                    node.left = dfs(l[1:i])
                    node.right = dfs(l[i:])

            return node
            
        return dfs(nl)