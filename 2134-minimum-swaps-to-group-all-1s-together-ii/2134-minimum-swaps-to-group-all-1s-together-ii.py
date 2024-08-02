class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        ans = inf

        cuml = [0 for _ in range(len(nums)*2)]
        cuml[0] = 0 if nums[0] else 1
        for i in range(1,len(nums)*2):
            cuml[i] = cuml[i-1] + (0 if nums[i%len(nums)] else 1)

        ocnt = len(nums)-cuml[len(nums)-1]

        for i in range(len(nums)):
            j = i+ocnt-1
            ans = min(ans,cuml[j] - (cuml[i-1] if i-1>=0 else 0))

        return ans

            
            