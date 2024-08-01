class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0

        for detail in details:
            age = int(detail[-4:-2])
            if age > 60:
                ans += 1

        return ans