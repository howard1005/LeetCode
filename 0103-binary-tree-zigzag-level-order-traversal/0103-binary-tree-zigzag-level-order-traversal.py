# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
   
        d = defaultdict(list)
        def dfs(node,lev):
            d[lev].append(node.val)
            if node.left:
                dfs(node.left,lev+1)
            if node.right:
                dfs(node.right,lev+1)
        dfs(root, 0)
        
        for lev in range(len(d)):
            if lev&1:
                d[lev].reverse()
            ans.append(d[lev])
        
        return ans