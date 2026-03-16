from heapq import heappush,heappop

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])

        # 0~25
        def cal(si,sj,edge_size):
            if edge_size == 0:
                return grid[si][sj]
            ret = 0
            i,j = si,sj
            for _ in range(edge_size):
                i-=1
                j+=1
                if i<0 or j<0 or i>=m or j>=n:
                    return -1 
                ret += grid[i][j]
            for _ in range(edge_size):
                i+=1
                j+=1
                if i<0 or j<0 or i>=m or j>=n:
                    return -1
                ret += grid[i][j]
            for _ in range(edge_size):
                i+=1
                j-=1
                if i<0 or j<0 or i>=m or j>=n:
                    return -1
                ret += grid[i][j]
            for _ in range(edge_size):
                i-=1
                j-=1
                if i<0 or j<0 or i>=m or j>=n:
                    return -1
                ret += grid[i][j]

            return ret
        
        sd = set()
        hq = []
        for size in range(min(m,n)+1):
            for i in range(m):
                for j in range(n):
                    a = cal(i,j,size)
                    if a != -1 and a not in sd:
                        sd.add(a)
                        heappush(hq,-a)
        
        ans = []
        for _ in range(3):
            if hq:
                ans.append(-heappop(hq))
        
        return ans
                
                
