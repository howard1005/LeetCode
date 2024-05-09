class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        
        m = (k-1)*k//2
        happiness.sort(reverse=True)
       
        for i in range(k):
            ans += max(0,happiness[i]-i)
    
        return ans