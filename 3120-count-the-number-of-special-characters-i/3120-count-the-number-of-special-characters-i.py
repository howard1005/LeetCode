class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0

        d = defaultdict(int)
        for c in word:
            d[c] += 1

        for a,b in zip(range(ord('a'),ord('z')+1),range(ord('A'),ord('Z')+1)):
            c,C = chr(a),chr(b)
            ans += min(d[c],d[C]) > 0

        return ans