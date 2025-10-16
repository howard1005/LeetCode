class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        MAX = 10**9
        
        d = defaultdict(int)

        for n in nums:
            m = (n+MAX*value)%value
            d[m]+=1

        for i in range(len(nums)+1):
            m = i%value
            if d[m] == 0:
                return i
            d[m] -= 1

        return -1