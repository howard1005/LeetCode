class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ans = 0
        
        dq = deque()
        cum = 0
        for i,(a,b) in enumerate(zip(startTime,endTime)):
            dq.append((i,a,b))
            cum += b-a
            while len(dq) > k:
                _,c,d = dq.popleft()
                cum -= d-c
            if len(dq) == k:
                j = dq[0][0]
                e1 = endTime[j-1] if j>0 else 0
                s2 = startTime[i+1] if i < len(startTime)-1 else eventTime
                # print(e1,s2,cum)
                ans = max(ans,s2-e1-cum)

        return ans

            

            
