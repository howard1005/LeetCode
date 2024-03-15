class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        zi = -1
        p = 1
        for i,num in enumerate(nums):
            if num == 0:
                if zi != -1:
                    return ans
                zi = i
            else:
                p *= num
        if zi != -1:
            ans[zi] = p
            return ans
        for i,num in enumerate(nums):
            if num:
                ans[i] = p//num
        return ans