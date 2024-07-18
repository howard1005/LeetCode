# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0

        def dfs(node,depth):
            nonlocal ans
            if not node.left and not node.right:
                return [depth]
            l1,l2 = [],[]
            if node.left:
                l1.extend(dfs(node.left,depth+1))
            if node.right:
                l2.extend(dfs(node.right,depth+1))

            for dep1 in l1:
                for dep2 in l2:
                    if dep1-depth + dep2-depth <= distance:
                        ans += 1

            return l1+l2

        dfs(root,0)

        return ans