class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ans = 0
        
        l = [i-j for i,j in zip(capacity,rocks)]
        l.sort()
        for i in l:
            if i <= additionalRocks:
                additionalRocks -= i
                ans += 1
            else:
                break
        
        return ans
        