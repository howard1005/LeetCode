# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pard = defaultdict(None)
        depd = defaultdict(list)
        def dfs(par,node,dep):
            pard[node.val] = par
            depd[dep].append(node)
            if node.left:
                dfs(node,node.left,dep+1)
            if node.right:
                dfs(node,node.right,dep+1)
        dfs(None,root,0)

        l = depd[max(depd.keys())]
        
        d = defaultdict(int)
        dq = deque(l)
        while dq:
            node = dq.popleft()
            d[node.val] += 1
            if d[node.val] == len(l):
                return node
            dq.append(pard[node.val])

        return None
            