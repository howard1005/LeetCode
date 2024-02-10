class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        d = {}
        for length in range(len(s)):
            for i in range(len(s)-length):
                if s[i] == s[i+length]:
                    if i+1<=i+length-1:
                        if (i+1,i+length-1) in d:
                            d[(i,i+length)] = 1
                            ans += 1
                    else:
                        d[(i,i+length)] = 1
                        ans += 1
        return ans
                        