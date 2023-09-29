class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        p = nums[0]
        flag = 0
        for n in nums:
            if p < n:
                if flag == -1:
                    return False
                flag = 1
            elif p > n:
                if flag == 1:
                    return False
                flag = -1
            p = n
        return True