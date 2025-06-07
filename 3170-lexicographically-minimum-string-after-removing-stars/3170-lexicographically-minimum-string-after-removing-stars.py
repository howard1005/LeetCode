from heapq import heappush,heappop

class Solution:
    def clearStars(self, s: str) -> str:
        ansl = ['' for _ in range(len(s))]
        
        hq = []

        for i,c in enumerate(s):
            if c == '*':
                heappop(hq)
            else:
                heappush(hq,(c,-i))

        for c,i in hq:
            i = -i
            ansl[i] = c

        return ''.join(ansl)