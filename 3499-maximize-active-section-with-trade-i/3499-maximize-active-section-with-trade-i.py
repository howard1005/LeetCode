class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = 0

        cnt = 0
        for c in s:
            if c == '1':
                cnt += 1
        ans = cnt

        l = []
        coni = 0
        for i in range(len(s)):
            c = s[i]
            if c == '0':
                pass
            else:
                if coni <= i-1:
                    l.append((coni,i-1))
                coni = i+1
        if coni < len(s):
            l.append((coni,len(s)-1))
        # print(l)

        for i in range(len(l)-1):
            ans = max(ans,cnt + l[i][1]-l[i][0] + l[i+1][1]-l[i+1][0] + 2)

        return ans