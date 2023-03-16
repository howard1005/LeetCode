# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inorder,postorder):
            if not inorder:
                return None
            idx = inorder.index(postorder[-1])
            return TreeNode(postorder[-1],dfs(inorder[:idx],postorder[:idx]),dfs(inorder[idx+1:],postorder[idx:-1]))
        return dfs(inorder,postorder)