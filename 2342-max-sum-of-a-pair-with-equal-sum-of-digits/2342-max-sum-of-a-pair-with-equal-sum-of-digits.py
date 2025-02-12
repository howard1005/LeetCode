class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1

        d = defaultdict(lambda:[0,0])

        def digit_sum(n):
            ret = 0
            while n:
                ret += n%10
                n //= 10
            return ret
        
        for n in nums:
            l = d[digit_sum(n)]
            if l[0] < n:
                n,l[0] = l[0],n
            if l[1] < n:
                n,l[1] = l[1],n

        for a,b in d.values():
            if b:
                ans = max(ans,a+b)
        
        return ans