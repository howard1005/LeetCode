from heapq import heappush,heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        
        th = []
        for i,(a,b) in enumerate(tasks):
            heappush(th,(a,b,i))
        
        ah = []
        now = 0
        while th or ah:
            while th and now >= th[0][0]:
                (a,b,i) = heappop(th)
                heappush(ah,(b,i,a))
            if not ah:
                if th:
                    now = th[0][0]
                    continue
                else:
                    break
            (b,i,a) = heappop(ah)
            ans.append(i)
            now += b
            
            
            
            
        return ans