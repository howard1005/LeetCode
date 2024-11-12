from heapq import heappush,heappop

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ansl = [0 for _ in range(len(queries))]
        
        h = []

        items.sort(key=lambda x: x[0])
        ql = [(q,i) for i,q in enumerate(queries)]
        ql.sort()
        

        i = 0
        for q,j in ql:
            while i < len(items):
                p,b = items[i]
                if p <= q:
                    heappush(h,-b)
                else:
                    break
                i += 1
            if h:
                ansl[j] = -h[0]
            
        return ansl