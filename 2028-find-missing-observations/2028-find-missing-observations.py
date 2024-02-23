class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        t = mean*(len(rolls)+n)-sum(rolls)-n
        
        ans = [1 for _ in range(n)]
        
        if t < 0:
            return []
        
        for i in range(n):
            m = min(t,5)
            ans[i] += m
            t -= m
        
        if t:
            return []
        
        return ans
            