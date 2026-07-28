class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = ['' for _ in range(len(s))]
        
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        i,j = 0,len(s)-1
        for n in range(26):
            c = chr(n+ord('a'))
            if d[c] > 1:
                cnt = d[c]
                while cnt>1:
                    l[i] = c
                    l[j] = c
                    cnt -= 2
                    i += 1
                    j -= 1
            if d[c]%2 == 1:
                l[len(s)//2] = c

        ans = ''.join(l)

        return ans

        