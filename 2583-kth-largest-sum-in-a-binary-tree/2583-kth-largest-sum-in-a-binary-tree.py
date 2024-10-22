# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        d = defaultdict(int)

        def dfs(node,dep):
            d[dep] += node.val
            if node.left:
                dfs(node.left,dep+1)
            if node.right:
                dfs(node.right,dep+1)

        dfs(root,0)

        l = list(d.values())
        
        if len(l) < k:
            return -1
        
        l.sort(reverse=True)

        return l[k-1]
        