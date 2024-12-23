# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

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

            pd = {}
            for i,v in enumerate(l):
                pd[v] = i

            for i,v in enumerate(sorted(l)):
                j = pd[v]
                if i == j:
                    continue
                tv = l[i]
                l[i],l[j] = l[j],l[i]
                pd[v],pd[tv] = i,j
                # print("swap i,j,")
                ans += 1

        return ans
                
                
