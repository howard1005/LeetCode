class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        
        d = defaultdict(list)

        for w in words:
            dd = defaultdict(int)
            for c in w:
                dd[c] += 1
            for c,cnt in dd.items():
                d[c].append(cnt)
        
        for c,l in d.items():
            if len(l) == len(words):
                for _ in range(min(l)):
                    ans.append(c)
        
        return ans        