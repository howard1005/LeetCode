class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0

        colors.extend(colors[:k-1])

        head = 0
        for i in range(1,len(colors)):
            if colors[i-1] == colors[i]:
                head = i
            if i-head+1 >= k:
                ans += 1
        return ans