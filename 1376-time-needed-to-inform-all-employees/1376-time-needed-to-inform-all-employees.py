class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ans = 0
        
        d = defaultdict(list)
        for i,p in enumerate(manager):
            d[p].append(i)
            
        dq = deque([(headID,0)])
        while dq:
            i,t = dq.popleft()
            ans = max(ans,t)
            for j in d[i]:
                dq.append((j,t+informTime[i]))
            
        return ans