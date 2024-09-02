class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        r = k%sum(chalk)
        for i,c in enumerate(chalk):
            r -= c
            if r < 0:
                return i
        return -1