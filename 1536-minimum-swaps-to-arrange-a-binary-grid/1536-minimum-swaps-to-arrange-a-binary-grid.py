from heapq import heappush,heappop

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        ans = 0
        
        m,n = len(grid),len(grid[0])
        
        d = defaultdict(list)

        for i in range(m):
            z = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 0:
                    z += 1
                else:
                    break
            d[z].append(i)

        sl = SortedList()
        hq = []
        for idx in d[n]:
            heappush(hq,(idx,n))
            
        for i in range(m):
            k = n-1-i
            for idx in d[k]:
                heappush(hq,(idx,k))
            if not hq:
                return -1
            j,cnt = heappop(hq)
            jj = sl.bisect_left(j)
            cur = j+len(sl)-jj
            ans += cur-i
            sl.add(j)

        return ans
            