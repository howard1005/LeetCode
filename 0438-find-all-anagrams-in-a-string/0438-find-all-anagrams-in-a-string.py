class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            d[c] = 0
        for c in p:
            d[c] += 1
        ans = []
        t,h = 0,0
        while h < len(s):
            c = s[h]
            d[c] -= 1
            if d[c] < 0:
                while d[c] != 0:
                    d[s[t]] += 1
                    t += 1
            if sum(d.values()) == 0:
                ans.append(t)
            h += 1
        return ans
        