from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = [0,0]

        cum = 0
        for n in nums:
            cum ^= n

        lb = cum & -cum

        for n in nums:
            if n & lb:
                ans[0] ^= n
            else:
                ans[1] ^= n

        return ans
