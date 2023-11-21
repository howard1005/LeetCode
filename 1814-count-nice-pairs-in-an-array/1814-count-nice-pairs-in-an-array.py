class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans = 0
        
        MOD = 1000000007
        
        def rev(n):
            ret = 0
            while n:
                ret = ret*10 + n%10
                n //= 10
            return ret
        
        d = defaultdict(int)
        for n in nums:
            d[n-rev(n)] += 1
            
        print(d)
        
        for cnt in d.values():
            ans += cnt*(cnt-1)//2
            ans %= MOD
            
        return ans
        
            