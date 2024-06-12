class Solution:
    def sortColors(self, nums: List[int]) -> None:
        mp = [0 for _ in range(3)]
        for n in nums:
            mp[n] += 1
        i = 0
        for j in range(len(nums)):
            while mp[i] == 0:
                i += 1
            if mp[i]:
                nums[j] = i
                mp[i] -= 1
        