class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = [0 for _ in range(100002)]
        for n in nums:
            if 0 < n and n <= 100000:
                l[n] = 1
        for i in range(1,100002):
            if l[i] == 0:
                return i
        
        
                
                