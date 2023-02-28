# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        
        d = defaultdict(list)
        
        def dfs(node):
            if node == None:
                return [None]
            ret = [node.val]
            ret.extend(dfs(node.left))
            ret.extend(dfs(node.right))
            d[tuple(ret)].append(node)
            return ret
                       
        dfs(root)
        
        for l in d.values():
            if len(l) >= 2:
                ans.append(l[-1])
                
            
        
        return ans