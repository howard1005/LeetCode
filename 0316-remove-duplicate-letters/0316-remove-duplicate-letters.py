from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d= defaultdict(int)
        for c in s:
            d[c] += 1
        vis = defaultdict(int)
        st = []
        for c in s:
            if vis[c]:
                d[c] -= 1
                continue
            while st and d[st[-1]] and st[-1]>c:
                vis[st[-1]]=0
                st.pop()
            if vis[c] == 0:
                st.append(c)
                vis[c]=1
            d[c] -= 1
        return ''.join(st)