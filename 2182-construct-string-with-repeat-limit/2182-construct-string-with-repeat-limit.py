from heapq import heappush,heappop

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = ''

        d = defaultdict(int)
        for c in s:
            d[c] += 1

        hq = []
        for c,cnt in d.items():
            heappush(hq,(-ord(c),c,cnt))

        repeat = 0
        prev = ''
        while hq:
            n,c,cnt = heappop(hq)
            n = -n
            if c == prev:
                repeat += 1
                if repeat > repeatLimit:
                    if not hq:
                        break
                    n2,c2,cnt2 = heappop(hq)
                    n2 = -n2
                    heappush(hq,(-n,c,cnt))

                    ans += c2
                    if cnt2-1:
                        heappush(hq,(-n2,c2,cnt2-1))

                    repeat = 1
                else:
                    ans += c
                    if cnt-1:
                        heappush(hq,(-n,c,cnt-1))
            else:
                ans += c
                if cnt-1:
                    heappush(hq,(-n,c,cnt-1))
                prev = c
                repeat = 1

        return ans