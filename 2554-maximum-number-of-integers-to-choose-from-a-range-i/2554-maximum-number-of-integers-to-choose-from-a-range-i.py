class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        
        sd = set(banned)

        cum = 0
        for i in range(1,n+1):
            if i in sd:
                continue
            if cum + i <= maxSum:
                ans += 1
                cum += i
            else:
                break
        
        return ans
        
        