# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        d = defaultdict(list)

        def dfs(node,h):
            d[h].append(node)
            if node.left:
                dfs(node.left,h+1)
            if node.right:
                dfs(node.right,h+1)

        dfs(root,0)

        for i in range(1,max(d)+1,2):
            d[i].reverse()

        for i in range(max(d)):
            for j,node in enumerate(d[i]):
                node.left = d[i+1][j*2]
                node.right = d[i+1][j*2+1]
                
        return root