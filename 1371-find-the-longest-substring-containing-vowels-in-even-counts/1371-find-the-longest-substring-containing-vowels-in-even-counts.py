class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        rid = {
            'a':0,
            'e':1,
            'i':2,
            'o':3,
            'u':4,
        }

        ans = 0

        d = defaultdict(lambda:inf)
        st = 0

        for i,c in enumerate(s):
            if c in rid:
                st ^= (1<<rid[c])
            if st == 0:
                ans = i+1

            if d[st] != inf:
                ans = max(ans,i-d[st])
            d[st] = min(d[st],i)

        return ans
                