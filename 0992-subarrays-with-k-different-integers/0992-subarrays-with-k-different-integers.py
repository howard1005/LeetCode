class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        
        da,db = defaultdict(int),defaultdict(int)
        a,b,c = 0,0,0
        while c < len(nums):
            nc = nums[c]
            da[nc] += 1
            db[nc] += 1
            while len(da) > k:
                na = nums[a]
                da[na] -= 1
                if da[na] == 0:
                    del da[na]
                a += 1
            while len(db) >= k:
                nb = nums[b]
                db[nb] -= 1
                if db[nb] == 0:
                    del db[nb]
                b += 1
            ans += b-a
            c += 1
            
        return ans
            
            