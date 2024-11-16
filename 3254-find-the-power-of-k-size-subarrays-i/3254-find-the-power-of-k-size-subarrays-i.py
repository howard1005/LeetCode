class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ansl = []

        def isPower(l):
            for i in range(1,k):
                if l[i-1]+1 != l[i]:
                    return False
            return True
        
        for i in range(len(nums)):
            if i+k > len(nums):
                break
            l = nums[i:i+k]
            if isPower(l):
                ansl.append(max(l))
            else:
                ansl.append(-1)

        return ansl