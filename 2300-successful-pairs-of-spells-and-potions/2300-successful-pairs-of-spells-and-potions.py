from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        
        potions.sort()
        
        for spell in spells:
            i = bisect_left(potions,success//spell + (1 if success%spell else 0))
            ans.append(len(potions)-i)
            
        return ans
        
        