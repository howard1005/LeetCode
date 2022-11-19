from math import sqrt,isclose

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) < 3:
            return trees
        
        trees.sort(key=lambda p:(p[1],p[0]))
        base = trees[0]
        # print(base)
        
        def getVector(base,p):
            return (p[0]-base[0],p[1]-base[1])
        
        def getSize(v):
            return sqrt(v[0]*v[0]+v[1]*v[1])
        
        def getNorm(v):
            size = getSize(v)
            return (v[0]/size,v[1]/size) if size else (0,0)
        
        def crossProduct(v1,v2):
            return v1[0]*v2[1]-v1[1]*v2[0]
        
        def cmp(p):
            v = getVector(base,p)
            c = 1 if v[0]<0 else 0
            uv = getNorm(v)
            cp = crossProduct((1,0),uv)
            if v[0]<0:
                cp = 2-cp
            return cp
           
        trees.sort(key=cmp)
        # print(trees)
        
        def tcmp(p1,p2):
            return isclose(p1[0],p2[0]) and isclose(p1[1],p2[1])
        
        def ccw(p1,p2,p3):
            v1 = getVector(p1,p2)
            v2 = getVector(p2,p3)
# print(p1,p2,p3,crossProduct(v1,v2),getNorm(v1),getNorm(v2))
            cp = crossProduct(v1,v2)
            if cp > 0 or (cp == 0 and tcmp(getNorm(v1), getNorm(v2))):
                return True
            return False
        
        st = []
        i = 0
        while i < len(trees):
            p3 = tuple(trees[i])
            # print(p3)
            if len(st) < 2:
                st.append(p3)
                i += 1
                continue
            if ccw(st[-2],st[-1],p3):
                st.append(p3)
                i += 1
            else:
                st.pop()
        
        v = getVector(base,st[-1])
        for tree in trees:
            p = tuple(tree)
            if crossProduct(v,getVector(base,p)) == 0:
                st.append(p)

        return set(st)