class Solution:
    def processStr(self, s: str, k: int) -> str:
        ans = ''

        le = 0
        for c in s:
            if c == '*':
                le -= 1
                le = max(0,le)
            elif c == '#':
                le *= 2
            elif c == '%':
                pass
            else:
                le += 1

        if le <= k:
            return '.'

        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if c == '*':
                le += 1
            elif c == '#':
                le //= 2
                k %= le
            elif c == '%':
                k = le-k-1
            else:
                if k == le-1:
                    return c
                le -= 1
            # print(i,k,le)

        return ans