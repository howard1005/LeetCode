class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = text.split()
        sd = set(brokenLetters)

        ans = len(l)
        
        for w in l:
            for c in w:
                if c in sd:
                    ans -= 1
                    break

        return ans
                    