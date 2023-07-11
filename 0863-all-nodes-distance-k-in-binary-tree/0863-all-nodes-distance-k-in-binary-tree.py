# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        
        pd = {}
        
        def dfs(node):
            if node.left:
                pd[node.left] = node
                dfs(node.left)
            if node.right:
                pd[node.right] = node
                dfs(node.right)
                
        pd[root] = None
        dfs(root)
        
        vis = {target:1}
        dq = deque([(target,0)])
        while dq:
            node,dist = dq.popleft()
            if dist == k:
                ans.append(node.val)
            for nn in [node.left,node.right,pd[node]]:
                if nn and nn not in vis:
                    vis[nn] = 1
                    dq.append((nn,dist+1))            
        
        return ans