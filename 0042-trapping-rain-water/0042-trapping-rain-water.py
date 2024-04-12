class Solution:
    def trap(self, height: List[int]) -> int:
        l = []
        ans = 0
        for i in range(len(height)):
            b = -1
            while l and l[-1][1] <= height[i]:
                idx,h = l.pop()
                if b == -1:
                    b = h
                else:
                    ans += (i - idx -1) * (h - b)
                    b = h
            if l:
                if b != -1 and b < height[i]:
                    ans += (i - l[-1][0] -1) * (height[i] - b)
            l.append((i,height[i]))
        return ans
                    
                    