# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        
        d = defaultdict(int)
        def dfs(node):
            d[node.val] += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        
        mx = max(d.values())
        for k,v in d.items():
            if v == mx:
                ans.append(k)
                
        
        return ans
        