from bisect import bisect_left,bisect_right

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans = 0
        
        l = [0 for _ in range(len(fruits))]
        l[0] = fruits[0][1]
        for i in range(1,len(l)):
            l[i] = fruits[i][1] + l[i-1]

        print(l)

        def cal(a,b):
            return (l[b] if b<len(l) else l[-1]) - (l[a-1] if a>0 else 0)

        def pos_left(p):
            i = bisect_left(fruits,p,key=lambda x:x[0])
            return i

        def pos_right(p):
            i = bisect_right(fruits,p,key=lambda x:x[0])
            return i-1

        
        i = 0

        while i<len(fruits) and fruits[i][0] <= startPos:
            p,cnt = fruits[i]
            dist = startPos - p
            if dist <= k:
                p2 = p + (k-dist)
                p2 = max(p2,startPos)
                # print(f"p2: {p2}")
                j = pos_right(p2)
                cum = cal(i,j)
                # print(p,cnt,j,i,cum)
                ans = max(ans,cum)
            i += 1

        while i<len(fruits):
            p,cnt = fruits[i]
            dist = p - startPos
            if p - startPos <= k:
                p2 = p - (k-dist)
                p2 = min(p2,startPos)
                # print(f"p2: {p2}")
                j = pos_left(p2)
                cum = cal(j,i)
                # print(p,cnt,j,i,cum)
                ans = max(ans,cum)
            i += 1

        return ans