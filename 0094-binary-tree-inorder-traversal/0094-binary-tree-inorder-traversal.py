# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def dfs(node):
            nonlocal ans
            if node.left:
                dfs(node.left)
            ans.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return ans