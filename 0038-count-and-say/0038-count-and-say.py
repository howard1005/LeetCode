class Solution:
    ansl = []
    def countAndSay(self, n: int) -> str:
        if not self.ansl:
            ansl = ['1']
            for _ in range(29):
                s = ansl[-1]
                ans = ''
                prev = ''
                cnt = 0
                for c in s:
                    if prev == c:
                        cnt += 1
                    else:
                        if cnt:
                            ans += '{}{}'.format(cnt,prev)
                        cnt = 1
                        prev = c
                if cnt:
                    ans += '{}{}'.format(cnt,prev)
                ansl.append(ans)
            self.ansl.extend(ansl)
            
        return self.ansl[n-1]
        