class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        ans = 0
        
        sd = set([stones[0],-stones[0]])
        for stone in stones[1:]:
            tsd = set()
            for t in sd:
                tsd.add(abs(t-stone))
                tsd.add(abs(t+stone))
            sd = tsd        
        
        return min(map(lambda x: abs(x),sd))
        