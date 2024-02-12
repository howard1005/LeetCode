from collections import defaultdict
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for k,v in d.items():
            if v >= math.ceil(len(nums)/2):
                return k