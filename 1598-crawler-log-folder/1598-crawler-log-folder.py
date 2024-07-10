class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0

        for log in logs:
            if log == '../':
                ans = max(ans-1,0)
            elif log == './':
                pass
            else:
                ans += 1

        return ans
