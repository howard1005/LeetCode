# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0
        
        ans = 0
        
        d = defaultdict(list)
        
        def dfs(node):
            if node.left:
                d[node.val].append(node.left)
                d[node.left.val].append(node)
                dfs(node.left)
            if node.right:
                d[node.val].append(node.right)
                d[node.right.val].append(node)
                dfs(node.right)
                
        dfs(root)
        
        vis = {start:1}
        dq = deque([(start,0)])
        while dq:
            n,cnt = dq.popleft()
            ans = cnt
            for nnode in d[n]:
                nn = nnode.val
                if nn not in vis:
                    vis[nn] = 1
                    dq.append((nn,cnt+1))
        
        return ans