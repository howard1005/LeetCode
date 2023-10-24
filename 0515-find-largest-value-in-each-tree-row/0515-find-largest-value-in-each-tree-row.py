# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        d = defaultdict(lambda :-inf)
        
        def dfs(node,h):
            d[h] = max(d[h],node.val)
            if node.left:
                dfs(node.left,h+1)
            if node.right:
                dfs(node.right,h+1)
        dfs(root,1)
                
        return [d[i] for i in range(1,len(d)+1)]