class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = ''
        for c in s:
            n = ord(c)-ord('a')+1
            ss += str(n)
        nn = int(ss)
        cum = 0
        for _ in range(k):
            while nn:
                cum += nn%10
                nn //= 10
            nn = cum
            cum = 0

        return nn

            