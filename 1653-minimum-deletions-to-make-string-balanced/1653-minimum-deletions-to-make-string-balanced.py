class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = inf

        al = [0 for _ in range(len(s))]
        bl = [0 for _ in range(len(s))]

        for i in range(len(s)):
            c = s[i]
            al[i] = al[max(i-1,0)]
            if c == 'b':
                al[i] += 1

        for i in range(len(s)-1,-1,-1):
            c = s[i]
            bl[i] = bl[min(i+1,len(s)-1)]
            if c == 'a':
                bl[i] += 1

        for i in range(len(s)):
            ans = min(ans,al[i]+bl[i]-1)

        return ans