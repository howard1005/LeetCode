# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = defaultdict(list)
        pard = {}

        def dfs(node,dep):
            d[dep].append(node)
            if node.left:
                pard[node.left.val] = node
                dfs(node.left,dep+1)
            if node.right:
                pard[node.right.val] = node
                dfs(node.right,dep+1)

        dfs(root,0)

        mx = max(d.keys())

        l = d[mx]

        ans = None

        while 1:
            sd = set(node.val for node in l)
            if len(sd) == 1:
                ans = l[0]
                break
            tl = []
            for node in l:
                tl.append(pard[node.val])
            l = tl

        return ans
                