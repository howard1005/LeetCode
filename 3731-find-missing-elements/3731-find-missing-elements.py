class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []

        sd = set(nums)

        for i in range(min(nums),max(nums)):
            if i not in sd:
                ans.append(i)

        ans.sort()

        return ans