from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] == 2:
                return num
        return -1