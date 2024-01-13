class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        
        sd,td = defaultdict(int),defaultdict(int)
        for c in s:
            sd[c] += 1
        for c in t:
            td[c] += 1
        
        for c in sd:
            diff = sd[c] - td[c]
            if diff > 0:
                ans += diff
        
        return ans