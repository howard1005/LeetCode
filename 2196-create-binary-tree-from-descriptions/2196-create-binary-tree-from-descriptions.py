# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = defaultdict(lambda:[None,None,None]) # p c1 c2
        
        for p,c,isl in descriptions:
            if isl:
                d[p][1] = c
            else:
                d[p][2] = c
            d[c][0] = p

        root = None
        for k,vl in d.items():
            if not vl[0]:
                root = k
                break

        def dfs(k):
            _,c1,c2 = d[k]
            c1node,c2node = None,None
            if c1:
                c1node = dfs(c1)
            if c2:
                c2node = dfs(c2)
            return TreeNode(k,c1node,c2node)

        return dfs(root)
        