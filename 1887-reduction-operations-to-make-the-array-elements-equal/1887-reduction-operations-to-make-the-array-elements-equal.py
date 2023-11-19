class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        if len(d) == 1:
            return 0
            
        l = [(k,v) for k,v in d.items()]
        l.sort(reverse=True)
        
        cums = [l[0][1]]
        for k,v in l[1:-1]:
            cums.append(cums[-1]+v)
        
        return sum(cums)