class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        pl = []
        nl = []
        
        for n in nums:
            if n>0:
                pl.append(n)
            else:
                nl.append(n)
        
        for p,n in zip(pl,nl):
            ans.extend([p,n])
            
        return ans