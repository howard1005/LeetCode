from heapq import heappush,heappop

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans =0
        
        i,j = 0,len(costs)-1
        f,l = [],[]
        for _ in range(candidates):
            if i > j:
                break
            heappush(f,(costs[i],i))
            i += 1
            if i > j:
                break
            heappush(l,(costs[j],j))
            j -= 1
        
        
        for _ in range(k):
            if f and f[0] == min(f[0], l[0] if l else (inf,inf)):
                ans += heappop(f)[0]
                if i <= j:
                    heappush(f,(costs[i],i))
                    i += 1
            elif l and l[0] == min(f[0] if f else (inf,inf), l[0]):
                ans += heappop(l)[0]
                if i <= j:
                    heappush(l,(costs[j],j))
                    j -= 1 
                
        return ans