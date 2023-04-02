from bisect import bisect_left,bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        ans = 0
        
        l = [nums[0]]
        for n in nums[1:]:
            l.append(l[-1]+n)
        
        for i in range(1,len(l)-1):
            right = l[-1]-l[i]
            a,b = l[i]-right,l[i]//2
            ai,bi = bisect_left(l,a,0,i-1),bisect_right(l,b,0,i-1)
            # print(i,a,b,ai,bi)
            if b < l[bi]:
                bi -= 1
            if a<=b and ai<=bi: 
                ans = (ans + bi-ai+1)%1000000007
                # print(ans)
        
        return ans