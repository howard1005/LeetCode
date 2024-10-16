from heapq import heappush,heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''

        h = []
        heappush(h,(-a,'a'))
        heappush(h,(-b,'b'))
        heappush(h,(-c,'c'))

        s = ''

        while 1:
            cnt,ch = heappop(h)
            if s[-2:] == ch*2:
                _cnt,_ch = heappop(h)
                heappush(h,(cnt,ch))
                cnt,ch = _cnt,_ch
            
            if cnt == 0:
                break

            s += ch
            heappush(h,(cnt+1,ch))

        ans = s
        
        return ans
            