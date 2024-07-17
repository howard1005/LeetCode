# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        sd = set(to_delete)

        def dfs(node):
            retl = [node] if node.val not in sd else []
            if node.left:
                l = dfs(node.left)
                if not l or l[0].val != node.left.val or node.val in sd:
                    node.left = None
                    retl.extend(l)
                else:
                    retl.extend(l[1:])
            if node.right:
                l = dfs(node.right)
                if not l or l[0].val != node.right.val or node.val in sd:
                    node.right = None
                    retl.extend(l)
                else:
                    retl.extend(l[1:])
            return retl

        return dfs(root)
                