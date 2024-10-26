from heapq import heappush,heappop

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        ansl = []
        
        d = {}
        dh = defaultdict(list)
        
        def dfs(node,dep):
            ret = dep
            d[node.val] = dep
            if node.left:
                ret = max(ret,dfs(node.left,dep+1))
            if node.right:
                ret = max(ret,dfs(node.right,dep+1))
            heappush(dh[dep],(-ret,node.val))
            return ret

        dfs(root,0)

        for q in queries:
            dep = d[q]
            h = dh[dep]
            if h[0][1] != q:
                ansl.append(-h[0][0])
            elif len(h) == 1:
                ansl.append(dep-1)
            else:
                t = heappop(h)
                ansl.append(-h[0][0])
                heappush(h,t)

        return ansl