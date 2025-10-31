class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        for k,v in d.items():
            if v == 2:
                ans.append(k)

        return ans