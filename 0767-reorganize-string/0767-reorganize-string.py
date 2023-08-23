from heapq import heappush,heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ' '
        
        d = defaultdict(int)
        for c in s:
            d[c] += 1
            
        hq = []
        for k,v in d.items():
            heappush(hq,(-v,k))
        
        while hq:
            cnt,c = heappop(hq)
            cnt = abs(cnt)
            if ans[-1] != c:
                ans += c
                if cnt-1:
                    heappush(hq,(-(cnt-1),c))
            else:
                if hq:
                    cnt2,c2 = heappop(hq)
                    cnt2 = abs(cnt2)
                    ans += c2
                    if cnt2-1:
                        heappush(hq,(-(cnt2-1),c2))
                    heappush(hq,(-(cnt),c))
                else:
                    return ''
        
        ans = ans[1:]
        return ans if len(ans) == len(s) else ''