class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            od,ed = defaultdict(int),defaultdict(int)
            n = nums[i]
            if n&1:
                od[n] += 1
            else:
                ed[n] += 1
            for j in range(i):
                n = nums[j]
                if n&1:
                    od[n] += 1
                else:
                    ed[n] += 1
            j = 0
            while len(od) != len(ed):
                n = nums[j]
                if n&1:
                    od[n] -= 1
                    if od[n] == 0:
                        del od[n]
                else:
                    ed[n] -= 1
                    if ed[n] == 0:
                        del ed[n]
                j += 1
            ans = max(ans,i-j+1)

        return ans
                
        
        
            
            