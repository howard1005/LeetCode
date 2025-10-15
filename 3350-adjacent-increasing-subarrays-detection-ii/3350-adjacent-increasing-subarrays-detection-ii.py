class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 0

        l = []
        
        si = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                pass
            else:
                l.append((si,i-1))
                si = i
        l.append((si,len(nums)-1))

        # print(l)

        last = None
        for a,b in l:
            size = b-a+1
            
            ans = max(ans,size//2)

            if last:
                if last[1]+1 == a:
                    ans = max(ans,min(last[1]-last[0]+1,size))

            last = (a,b)
        
        return ans
