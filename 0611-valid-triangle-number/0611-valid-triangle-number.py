class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == 0:
                continue
            k = i+2
            for j in range(i+1,len(nums)):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k-j-1
        return ans