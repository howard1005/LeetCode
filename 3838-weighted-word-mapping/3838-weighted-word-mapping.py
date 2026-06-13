class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''            
        for w in words:
            cum = 0
            for c in w:
                cum += weights[ord(c)-ord('a')]
            ans += chr((25-cum%26)+ord('a'))
        return ans