class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        l = []
        
        si = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                pass
            else:
                l.append((si,i-1))
                si = i
        l.append((si,len(nums)-1))

        cnt = 0
        for a,b in l:
            size = b-a+1
            if size>=2*k:
                return True
            if size>=k:
                cnt += 1
        
        return cnt >= 2

            