class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag = True
        for n in nums:
            if n != 1:
                flag = False
                break
        if flag:
            return len(nums)-1
        
        ans = 0
        
        l = []
        head = -1
        
        for i,n in enumerate(nums):
            if n == 0:
                a,b = head+1,i-1
                if a<=b:
                    l.append((a,b))
                head = i
            else:
                ans = max(ans,i-head)
        a,b = head+1,i
        if a<=b:
            l.append((a,b))
        ans = max(ans,i-head)
        
        for i in range(len(l)-1):
            (s1,e1),(s2,e2) = l[i],l[i+1]
            if s2-e1 == 2:
                ans = max(ans,e2-s1)
        
        return ans