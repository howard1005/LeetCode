from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = inf
        
        nums.sort()
        
        d = {nums[0]:0}
        cums = [0 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            cums[i] = cums[i-1]
            if nums[i-1] == nums[i]:
                cums[i] += 1
            else:
                d[nums[i]] = i
            
        def get_dup_cnt(i,j):
            return cums[j]-(cums[i-1] if i>0 else 0)
        
        # print(nums)
        for a,i in d.items():
            b = a+len(nums)-1
            j = bisect_right(nums,b)
            ans = min(ans,i+len(nums)-j+get_dup_cnt(i,j-1))
            # print(a,b,i,j,ans)
            
        return ans