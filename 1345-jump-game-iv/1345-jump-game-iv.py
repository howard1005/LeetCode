from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        for i,n in enumerate(arr):
            d[n].append(i)
        vis = [0 for _ in range(len(arr))]
        vis[0] = 1
        dq = deque([(0,0)])
        while dq:
            i,step = dq.popleft()
            if i == len(arr)-1:
                return step
            if i-1 >= 0 and vis[i-1] == 0:
                vis[i-1] = 1
                dq.append((i-1,step+1))
            if i+1 < len(arr) and vis[i+1] == 0:
                vis[i+1] = 1
                dq.append((i+1,step+1))
            for j in d[arr[i]]:
                if vis[j] == 0:
                    vis[j] = 1
                    dq.append((j,step+1))
            d[arr[i]].clear()
        return -1
                
        
        
        