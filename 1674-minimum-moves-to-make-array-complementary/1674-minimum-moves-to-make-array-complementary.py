class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        ans = inf
        
        l = [0 for _ in range(limit*2+1)]
        l[0] = len(nums)

        for i in range(len(nums)//2):
            a,b = nums[i],nums[len(nums)-1-i]
            lo,hi = max(a,b)-1,limit-min(a,b)
            m = a+b
            i,j = m-lo,m+hi
            l[i] -= 1
            l[m] -= 1
            if m+1 < len(l):
                l[m+1] += 1
            if j+1 < len(l):
                l[j+1] += 1

        for i in range(1,len(l)):
            l[i] += l[i-1]
            ans = min(ans,l[i])

        return ans
            
