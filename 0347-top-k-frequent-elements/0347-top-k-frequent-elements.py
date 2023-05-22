from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for n in nums:
            d[n]+=1
        return [n for cnt,n in list(reversed(sorted([(v,k) for k,v in d.items()])))[:k]]
        