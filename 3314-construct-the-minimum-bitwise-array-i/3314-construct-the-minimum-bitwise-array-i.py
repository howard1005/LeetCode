class Solution:
    d = {}
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        if not self.d:
            for i in range(10001):
                o = i|(i+1)
                if o not in self.d:
                    self.d[o] = i
        
        ans = []

        for n in nums:
            if n in self.d:
                ans.append(self.d[n])
            else:
                ans.append(-1)

        return ans

        