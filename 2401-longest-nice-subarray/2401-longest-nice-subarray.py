class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        
        l = []
        for n in nums:
            i = 0
            nd = {}
            while n:
                if n&1:
                    nd[i] = 1
                n >>= 1
                i += 1
            l.append(nd)
        
        d = defaultdict(int)

        j = 0
        for i in range(len(l)):
            nd = l[i]
            for k,v in nd.items():
                d[k] += v
                while j<i and d[k] > 1:
                    for kk,vv in l[j].items():
                        d[kk] -= vv
                    j += 1
            ans = max(ans,i-j+1)

        return ans

            