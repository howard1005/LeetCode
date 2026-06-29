class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0

        sd = set()

        for i in range(len(word)):
            for j in range(i+1,len(word)+1):
                sd.add(word[i:j])

        for p in patterns:
            if p in sd:
                ans += 1
        
        return ans