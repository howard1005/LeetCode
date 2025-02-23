# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(pre,post):
            if not pre or not post:
                return None
            v = pre[0]

            node = TreeNode(v)

            if len(pre) == 1:
                return node

            l1,l2 = pre[1:],post[:-1]

            lv = l1[0]
            for i in range(len(l2)):
                if l2[i] == lv:
                    a,b = l1[:i+1],l2[:i+1]
                    c,d = l1[i+1:],l2[i+1:]
                    node.left = dfs(a,b)
                    node.right = dfs(c,d)
                    break

            return node

        return dfs(preorder,postorder)
            