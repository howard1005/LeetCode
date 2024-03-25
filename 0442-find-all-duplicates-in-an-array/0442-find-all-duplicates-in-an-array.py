from collections import defaultdict

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] > 1:
                ans.append(num)
        return ans