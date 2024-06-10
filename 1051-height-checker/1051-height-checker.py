class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0

        for h1,h2 in zip(heights,sorted(heights)):
            ans += h1!=h2
        
        return ans