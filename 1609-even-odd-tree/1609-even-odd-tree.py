# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        d = defaultdict(list)
        
        def dfs(node,h):
            d[h].append(node.val)
            if node.left:
                dfs(node.left,h+1)
            if node.right:
                dfs(node.right,h+1)
        
        dfs(root,0)
        
        for i in range(len(d)):
            l = d[i]
            for j in range(len(l)):
                if i&1:
                    if l[j]&1:
                        return False
                else:
                    if l[j]&1==0:
                        return False
            for j in range(len(l)-1):
                if i&1:
                    if l[j] <= l[j+1]:
                        return False
                else:
                    if l[j] >= l[j+1]:
                        return False
                    
        return True
                
