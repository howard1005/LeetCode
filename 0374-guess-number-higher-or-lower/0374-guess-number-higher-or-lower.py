# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo=1
        hi=n
        while lo<=hi:
            mi = (lo+hi)//2
            chk = guess(mi)
            if chk == 1:
                lo = mi+1
            elif chk == -1:
                hi = mi-1
            else:
                return mi