class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        d = defaultdict(int)
        
        for i in range(len(nums)):
            cum = 0
            for j in range(i,len(nums)):
                cum += nums[j]
                d[cum] += 1
        
        l = []
        for n in range(min(d),max(d)+1):
            if n in d:
                l.extend([n]*d[n])

        return sum(l[left-1:right])