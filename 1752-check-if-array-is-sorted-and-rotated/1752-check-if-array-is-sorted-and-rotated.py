class Solution:
    def check(self, nums: List[int]) -> bool:
        size = len(nums)
        
        def valid(i):
            for _ in range(size-1):
                if nums[i%size] > nums[(i+1)%size]:
                    return False
                i += 1
            return True
        
        for i in range(size):
            if valid(i):
                return True
        
        return False