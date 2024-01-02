class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        d = defaultdict(int)
        
        for n in nums:
            d[n] += 1
        
        cnt = 0
        while cnt < len(nums):
            r = []
            for k,v in d.items():
                if v > 0:
                    r.append(k)
                    d[k] = v-1
                    cnt += 1
            ans.append(r)
        
        return ans