# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = defaultdict(lambda: defaultdict(int))
        td = defaultdict(int)

        def dfs1(par,node,dep):
            dd = d[dep]
            dd[id(par)] += node.val
            td[dep] += node.val

            if node.left:
                dfs1(node, node.left,dep+1)
            if node.right:
                dfs1(node, node.right,dep+1)

        dfs1(None,root,0)

        def dfs2(par,node,dep):
            dd = d[dep]
            node.val = td[dep] - dd[id(par)]

            if node.left:
                dfs2(node, node.left,dep+1)
            if node.right:
                dfs2(node, node.right,dep+1)

        dfs2(None,root,0)

        return root