class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        l = []
        for i,t in enumerate(temperatures):
            while l and l[-1][1] < t:
                j = l.pop()[0]
                ans[j] = i-j
            l.append((i,t))
        return ans