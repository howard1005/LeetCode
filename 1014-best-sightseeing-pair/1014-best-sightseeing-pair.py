class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0

        mx = 0
        for i,v in enumerate(values):
            ans = max(ans,mx+v-i)
            mx = max(mx,i+v)

        return ans