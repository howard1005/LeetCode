class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ansl = []

        d = defaultdict(int)

        for w in words:
            s = ''
            for c in w:
                s += c
                d[s] += 1
        
        for w in words:
            s = ''
            cnt = 0
            for c in w:
                s += c
                cnt += d[s]
            ansl.append(cnt)

        return ansl
                
        