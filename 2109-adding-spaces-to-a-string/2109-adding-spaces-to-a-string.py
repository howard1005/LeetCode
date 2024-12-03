class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''

        sd = set(spaces)

        for i,c in enumerate(s):
            if i in sd:
                ans += ' '
            ans += c

        return ans