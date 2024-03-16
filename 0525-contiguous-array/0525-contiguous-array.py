class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l = [0 for _ in range(len(nums))]
        l[0] = 1 if nums[0] else -1
        for i in range(1,len(nums)):
            l[i] = l[i-1] + (1 if nums[i] else -1)
        print(l)
        ans = 0
        d = {}
        for i in range(len(l)):
            if l[i] == 0:
                ans = max(ans,i+1)
            else:
                if l[i] in d:
                    ans = max(ans,i-d[l[i]])
            if l[i] not in d:
                d[l[i]] = i
        return ans