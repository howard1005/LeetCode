from math import sqrt,isclose

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) < 3:
            return trees
        
        trees.sort(key=lambda p:(p[1],p[0]))
        
        def getVector(base,p):
            return (p[0]-base[0],p[1]-base[1])
        
        def crossProduct(v1,v2):
            return v1[0]*v2[1]-v1[1]*v2[0]
        
        def ccw(p1,p2,p3):
            v1 = getVector(p1,p2)
            v2 = getVector(p1,p3)
            return crossProduct(v1,v2) >= 0
        
        def proc(points):
            st = []
            for p in points:
                p3 = tuple(p)
                while len(st)>=2 and not ccw(st[-2],st[-1],p3):
                    st.pop()
                st.append(p3)
            return st

        return set(proc(trees)+proc(trees[::-1]))