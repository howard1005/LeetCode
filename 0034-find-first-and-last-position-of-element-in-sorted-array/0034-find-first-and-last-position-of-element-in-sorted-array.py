class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        def upper():
            u = len(nums) - 1
            l = 0
            ret = -1
            while l <= u:
                m = int((u+l)/2)
                if nums[m] == target:
                    ret = m
                    l = m+1
                elif nums[m] < target:
                    l = m+1
                else:
                    u = m - 1
            return ret
        def lower():
            u = len(nums) - 1
            l = 0
            ret = -1
            while l <= u:
                m = int((u+l)/2)
                print(l,u)
                if nums[m] == target:
                    ret = m
                    u = m - 1
                elif nums[m] < target:
                    l = m+1
                else:
                    u = m - 1
            return ret
        return [lower(),upper()]
        