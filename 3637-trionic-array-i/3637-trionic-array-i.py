class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        f = 0

        if nums[0] >= nums[1]:
            return False

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                if f%2 == 0:
                    pass
                elif f == 1:
                    f += 1
                else:
                    return False
            elif nums[i] > nums[i+1]:
                if f == 1:
                    pass
                elif f == 0:
                    f += 1
                else:
                    return False
            else:
                return False

        return True if f >= 2 else False
                    