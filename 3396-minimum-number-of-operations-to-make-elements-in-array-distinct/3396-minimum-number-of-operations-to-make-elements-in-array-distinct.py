class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for k,v in d.copy().items():
            d[k] -= 1
            if d[k] == 0:
                del d[k]
        i = 0
        while d:
            ans += 1
            for _ in range(3):
                if i == len(nums):
                    break
                n = nums[i]
                if n in d:
                    d[n] -= 1
                    if d[n] == 0:
                        del d[n]
                i += 1

        return ans