class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        ans = ''

        d = defaultdict(int)
        for c in s:
            d[c] += 1

        # print(d)
        
        odd = 0
        oddc = ''
        for k,v in d.items():
            # print(k,v)
            if v&1:
                odd += 1
                oddc = k
            d[k] = d[k]//2
        # print(odd)
        if odd > 1:
            return ''

        # print(d)

        size = len(s)

        hi = size//2 

        chrs = sorted(d.keys())

        def dfs(i):
            if i == hi:
                mid = oddc if odd else ''
                candidate = target[:hi] + mid + target[:hi][::-1]

                return mid if candidate > target else None
                

            t = target[i]

            for c in chrs:
                if c < t or d[c] == 0:
                    continue

                if c > t:
                    d[c] -= 1
                    tl = []
                    for k,v in d.items():
                        tl.extend([k]*v)
                    tl.sort()
                    return c + ''.join(tl) + oddc

                d[c] -= 1
                suf = dfs(i+1)
                d[c] += 1

                if suf == None:
                    continue

                return c + suf

            return None

        hf = dfs(0)

        if not hf:
            return ''

        if size&1:
            ans = hf + hf[:-1][::-1]
        else:
            ans = hf + hf[::-1]

        return ans if ans > target else ''