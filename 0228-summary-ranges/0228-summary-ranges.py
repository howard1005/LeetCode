class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        s,e = nums[0],nums[0]
        def makeRange():
            nonlocal ans,s,e
            if s == e:
                ans.append(str(s))
            else:
                ans.append('{}->{}'.format(s,e))

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                e = nums[i]
            else:
                makeRange()
                s = e = nums[i]
        makeRange()
        return ans

                    