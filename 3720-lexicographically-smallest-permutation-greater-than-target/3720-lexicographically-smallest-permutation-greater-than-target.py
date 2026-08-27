class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        ans = ''

        d = defaultdict(int)
        for c in s:
            d[c] += 1

        l = list(d.keys())
        l.sort()

        def dfs(i):
            # print(i)
            if i == len(s):
                return ''

            t = target[i]

            for c in l:
                if t > c or d[c] == 0:
                    continue
                
                if c > t:
                    tl = []
                    d[c] -= 1
                    for k,v in d.items():
                        tl.extend([k]*v)
                    tl.sort()
                    return c + ''.join(tl)

                d[c] -= 1
                r = dfs(i+1)
                d[c] += 1

                if r:
                    return c+r

            return ''

        ans = dfs(0)

        return ans if ans else ''