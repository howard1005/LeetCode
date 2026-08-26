class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ''

        mn = inf
        cands = []

        i,j = 0,0

        cnt = 0
        while j<len(s):
            if s[j] == '1':
                cnt += 1
            while i <= j and cnt > k:
                if s[i] == '1':
                    cnt -= 1
                i += 1
            while i <= j and s[i] == '0':
                i += 1
            # print(i,j,cnt)
            size = j-i+1
            if cnt == k and mn >= size:
                if size != mn:
                    cands.clear()
                    mn = size
                cands.append(s[i:j+1])
            j += 1

        if cands:
            ans = min(cands)
            
        return ans
                