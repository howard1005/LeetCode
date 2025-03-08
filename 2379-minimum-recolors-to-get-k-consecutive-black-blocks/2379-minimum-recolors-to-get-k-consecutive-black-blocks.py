class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = inf
        for i in range(len(blocks)):
            wcnt = 0
            if i+k > len(blocks):
                break
            for j in range(i,i+k):
                if blocks[j] == 'W':
                    wcnt += 1
            ans = min(ans,wcnt)
        return ans