class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(w1,w2):
            if len(w1) > len(w2):
                return False
            size = len(w1)
            if w1 == w2[:size] and w1 == w2[-size:]:
                return True
            return False
        
        ans = 0

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                w1,w2 = words[i],words[j]
                if isPrefixAndSuffix(w1,w2):
                    ans += 1

        return ans
                