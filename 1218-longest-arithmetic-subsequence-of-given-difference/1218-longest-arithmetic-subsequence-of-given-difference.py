class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 0
        
        d = defaultdict(int)
        
        for n in arr[::-1]:
            d[n] = d[n + difference] + 1
            ans = max(ans,d[n])
            
        return ans