class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = sorted([(v,i) for i,v in enumerate(nums)])
        i = 0
        j = len(l) - 1
        while 1:
            _sum = l[i][0] + l[j][0]
            if _sum == target:
                return [l[i][1],l[j][1]]
            elif _sum < target:
                i += 1
            else:
                j -= 1