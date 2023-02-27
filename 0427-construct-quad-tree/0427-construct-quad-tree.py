"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(r1,r2):
            if r1[0] == r1[1] and r2[0] == r2[1]:
                return Node(grid[r1[0]][r2[0]],True,None,None,None,None)
            
            m1 = (r1[0]+r1[1])//2
            m2 = (r2[0]+r2[1])//2
            l = [
                dfs((r1[0],m1), (r2[0],m2)),
                dfs((r1[0],m1), (m2+1,r2[1])),
                dfs((m1+1,r1[1]), (r2[0],m2)),
                dfs((m1+1,r1[1]), (m2+1,r2[1]))
            ]
            
            if len(list(filter(lambda x:x.isLeaf, l))) == 4:
                if sum(map(lambda x:x.val, l)) in [0,4]:
                    return Node(l[0].val,True,None,None,None,None)
                
            return Node(0,
                        False,
                        l[0],
                        l[1],
                        l[2],
                        l[3]
                       )
        
        root = dfs((0,len(grid)-1),(0,len(grid[0])-1))

        return root