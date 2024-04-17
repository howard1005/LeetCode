# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        mn = [25 for _ in range(100)]
        
        def dfs(node,l):
            nonlocal mn
            ll = [node.val]+l
            if not node.left and not node.right:
                mn = min(mn,ll)
            if node.left:
                dfs(node.left,ll)
            if node.right:
                dfs(node.right,ll)
                
        dfs(root,[])
        
        return ''.join([chr(ord('a')+n) for n in mn])
            
            