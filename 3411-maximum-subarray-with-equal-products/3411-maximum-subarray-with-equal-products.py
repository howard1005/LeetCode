from math import gcd,lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0

        def valid(arr):
            g,l = 2*3*4*5*6*7*8*9*10,1
            p = 1
            for a in arr:
                p *= a
                g = gcd(g,a)
                l = lcm(l,a)
            # print(arr,p,g,l,p == g*l)
            return True if p == g*l else False
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if valid(nums[i:j]):
                    ans = max(ans,j-i)
            
        return ans