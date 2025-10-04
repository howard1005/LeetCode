class Solution:
    def maxArea(self, height: List[int]) -> int:
        l1 = [-1 for _ in range(10001)]
        l2 = [float('inf') for _ in range(10001)]
        for i,h in enumerate(height):
            l1[h] = max(l1[h],i)
            l2[h] = min(l2[h],i)
        for i in range(len(l1)-2,-1,-1):
            l1[i] = max(l1[i],l1[i+1])
            l2[i] = min(l2[i],l2[i+1])
        ans = 0
        for i,h in enumerate(height):
            if l1[h] != -1:
                ans = max(ans,(l1[h] - i)*h)
            if l2[h] != float('inf'):
                ans = max(ans,(i - l2[h])*h)
        return ans