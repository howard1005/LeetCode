class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cnt = inf
        for n in nums:
            if n == 1:
                if cnt < k:
                    return False
                cnt = 0
            else:
                cnt += 1

        return True