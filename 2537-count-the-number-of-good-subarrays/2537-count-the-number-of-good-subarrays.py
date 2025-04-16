class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0

        d = defaultdict(int)
        
        i = 0
        cnt = 0
        for j,n in enumerate(nums):
            cnt += d[n]
            d[n] += 1
            while i<j:
                m = nums[i]
                if cnt-(d[m]-1) < k:
                    break
                cnt -= (d[m]-1)
                d[m] -= 1
                i += 1
            if cnt >= k:
                ans += i+1

        return ans
        
        