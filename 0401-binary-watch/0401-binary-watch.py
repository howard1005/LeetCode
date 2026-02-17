from itertools import combinations


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        
        for c in combinations([i for i in range(10)], turnedOn):
            # 0~5:분 6~9:시
            h,m = 0,0
            for b in c:
                if b<=5:
                    m += (1<<b)
                else:
                    h += (1<<(b-6))
            if h>11 or m>59:
                continue
            t = "{}".format(h) + ":" + "{:02d}".format(m)
            ans.append(t)

        return ans