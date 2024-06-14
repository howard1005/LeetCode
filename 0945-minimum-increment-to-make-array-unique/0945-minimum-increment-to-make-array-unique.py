class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        
        nums.sort()
        mx = 0
        d = set()
        for n in nums:
            if n in d:
                ans += mx+1-n
                mx += 1
                d.add(mx)
            else:
                d.add(n)
                mx = max(mx,n)        
        
        return ans