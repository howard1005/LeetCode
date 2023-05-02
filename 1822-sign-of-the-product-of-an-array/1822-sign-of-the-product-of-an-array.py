class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                cnt += 1
        return 1 if cnt % 2 == 0 else -1