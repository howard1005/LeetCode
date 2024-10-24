# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        d = defaultdict(lambda:None)

        def get_val(node):
            if not node:
                return None
            return node.val

        def dfs1(node):
            d[get_val(node)] = node
            if node.left:
                dfs1(node.left)
            if node.right:
                dfs1(node.right)

        dfs1(root1)

        def valid(node1,node2):
            if get_val(node1.left) == get_val(node2.left) and get_val(node1.right) == get_val(node2.right):
                return True
            if get_val(node1.left) == get_val(node2.right) and get_val(node1.right) == get_val(node2.left):
                return True
            return False
            

        def dfs2(node):
            ret = True
            node1 = d[get_val(node)]
            if not node1:
                return False
            if not valid(node1,node):
                return False
            if node.left:
                ret &= dfs2(node.left)
            if node.right:
                ret &= dfs2(node.right)

            return ret

        ans = dfs2(root2)

        return ans
