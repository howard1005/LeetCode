class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        d = defaultdict(list)
        ind = [0 for _ in range(n)]
        for a,b in relations:
            d[a-1].append(b-1)
            ind[b-1] += 1
        
        dq = deque()
        for i,cnt in enumerate(ind):
            if cnt == 0:
                dq.append(i)
                
        l = [0 for _ in range(n)]
        while dq:
            i = dq.popleft()
            t = time[i] + l[i]
            for j in d[i]:
                ind[j] -= 1
                l[j] = max(l[j],t)
                if ind[j] == 0:
                    dq.append(j)
        
        ans = 0
        
        for t,cum in zip(time,l):
            ans = max(ans,t+cum)
        
        return ans
                
        
        
        
        
        
        
        
        