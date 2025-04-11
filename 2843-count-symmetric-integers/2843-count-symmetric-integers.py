class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for n in range(low,high+1):
            s = str(n)
            if len(s)&1:
                continue
            i = len(s)//2
            sum(int(c) for c in s[:i])
            if sum(int(c) for c in s[:i]) == sum(int(c) for c in s[i:]):
                ans += 1
        return ans