from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        
        d = defaultdict(int)
        d[0] = 1
        cum = 0
        for n in nums:
            cum += n
            remain = cum%k
            ans += d[remain]
            d[remain] += 1
        
        return ans