class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        
        sd = set(allowed)

        def valid(w):
            for c in w:
                if c not in sd:
                    return False
            return True

        for w in words:
            if valid(w):
                ans += 1

        return ans

                    