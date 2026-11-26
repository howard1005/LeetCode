class Solution:
    def canAliceWin(self, n: int) -> bool:
        cnt = 10
        while n>=0:
            n -= cnt
            if n < 0:
                return True if cnt%2 == 1 else False
            cnt -= 1
        return False