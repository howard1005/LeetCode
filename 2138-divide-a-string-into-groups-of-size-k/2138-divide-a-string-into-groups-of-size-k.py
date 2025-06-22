class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []

        t = ''
        for c in s:
            t += c
            if len(t) == k:
                ans.append(t)
                t = ''
        if t:
            ans.append(t)

        size = len(ans[-1])
        if size != k:
            ans[-1] += (fill*(k-size))

        return ans