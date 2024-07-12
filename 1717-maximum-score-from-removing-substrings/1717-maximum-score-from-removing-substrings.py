class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0

        def proc1(ss):
            acnt = ss.count('a')
            bcnt = ss.count('b')
            n = 0
            cnt = 0
            for c in ss:
                if c == 'a':
                    cnt += 1
                if c == 'b':
                    if cnt:
                        cnt -= 1
                        n += x
                        acnt -= 1
                        bcnt -= 1
            n += min(acnt,bcnt)*y
            return n
        
        def proc2(ss):
            acnt = ss.count('a')
            bcnt = ss.count('b')
            n = 0
            cnt = 0
            for c in ss:
                if c == 'b':
                    cnt += 1
                if c == 'a':
                    if cnt:
                        cnt -= 1
                        n += y
                        acnt -= 1
                        bcnt -= 1
            n += min(acnt,bcnt)*x
            return n
            
        l = []
        ss = ''
        for c in s:
            if c in 'ab':
                ss += c
            else:
                l.append(ss)
                ss = ''
        if ss:
            l.append(ss)

        for ss in l:
            ans += max(proc1(ss),proc2(ss))

        return ans
                
            
        