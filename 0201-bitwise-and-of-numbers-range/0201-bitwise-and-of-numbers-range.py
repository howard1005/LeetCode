class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        i = 0
        while left or right:
            if left == right and (left&1):
                ans |= (1<<i)
            left >>= 1
            right >>= 1
            i += 1
        return ans