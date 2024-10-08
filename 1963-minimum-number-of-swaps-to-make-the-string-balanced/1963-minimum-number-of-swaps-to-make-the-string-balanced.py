class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        o = 0
        for c in s:
            if c == '[':
                o += 1
            else:
                if o == 0:
                    o += 1
                    ans += 1
                else:
                    o -= 1
        print(ans,o)
        return ans