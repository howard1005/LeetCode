class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(list)

        def digitSum(m):
            ret = 0
            while m:
                ret += m%10
                m //= 10
            return ret

        for i in range(1,n+1):
            s = digitSum(i)
            d[s].append(i)
        
        mx = max(len(l) for k,l in d.items())
        
        ans = 0

        for k,l in d.items():
            if len(l) == mx:
                ans += 1

        return ans