class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = defaultdict(int)
        
        for n in arr:
            d[n] += 1
            
        ans = 0
        mx = 0
        for k,v in d.items():
            if mx < v:
                ans = k
                mx = v
        
        return ans