from bisect import bisect_left

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0

        n = len(fruits)
        
        size = 1
        while size<=n:
            size *= 2
        # print(size)

        tree = [inf for _ in range(size*2+1)]

        def req(i,s,e,qs,qe):
            if qe < s or e < qs:
                return inf
            if qs <= s and e <= qe:
                return tree[i]

            m = (s+e)//2
            v1 = req(i*2,s,m,qs,qe)
            v2 = req(i*2+1,m+1,e,qs,qe)

            return min(v1,v2)
            

        def update(i,s,e,qs,qe,v):
            if qe < s or e < qs:
                return tree[i]
            if qs <= s and e <= qe:
                tree[i] = v
                return tree[i]
            
            m = (s+e)//2
            v1 = update(i*2,s,m,qs,qe,v)
            v2 = update(i*2+1,m+1,e,qs,qe,v)

            tree[i] = min(v1,v2)

            # print(f"update {i},{s},{e},{v1},{v2}, {tree[i]}")

            return tree[i]

            
        l = [(v,i) for i,v in enumerate(baskets)]
        l.sort()
        # print(l)
        
        d = {}

        for i,(v,j) in enumerate(l):
            d[j] = i
            update(1,0,size-1,i,i,j)


        for f in fruits:
            i = bisect_left(l,f,key=lambda x:x[0])
            
            j = req(1,0,size-1,i,size-1)
            # print(tree,f,i,j)
            if j != inf:
                k = d[j]
                update(1,0,size-1,k,k,inf)
            else:
                ans += 1

        return ans