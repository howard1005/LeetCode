class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = inf
        
        l = [0 for _ in range(len(customers)+1)]
        l[0] = 1 if customers[0] == 'N' else 0
        for i in range(1,len(customers)):
            l[i] += l[i-1] + (1 if customers[i] == 'N' else 0)
        l[-1] = l[-2]
            
        rl = [0 for _ in range(len(customers)+1)]
        rl[-2] = 1 if customers[-1] == 'Y' else 0
        for i in range(len(customers)-2,-1,-1):
            rl[i] += rl[i+1] + (1 if customers[i] == 'Y' else 0)
        
        incur = inf
        for i in range(len(l)):
            t = (l[i-1] if i-1>=0 else 0) + rl[i]
            if incur > t:
                incur = t
                ans = i

        return ans