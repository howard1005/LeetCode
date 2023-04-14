class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ans = 1
        
        d = defaultdict(int)
        for i in range(len(s)):
            d[(i,i)] = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                d[(i,i+1)] = 2
                ans = 2
            else:
                d[(i,i+1)] = 1
        
        for size in range(2,len(s)):
            for i in range(len(s)-size):
                j = i + size
                d[(i,j)] = max(d[(i+1,j)],d[(i,j-1)])
                if s[i] == s[j]:
                    d[(i,j)] = max(d[(i,j)], d[(i+1,j-1)]+2)
                ans = max(ans, d[(i,j)])
        
        return ans