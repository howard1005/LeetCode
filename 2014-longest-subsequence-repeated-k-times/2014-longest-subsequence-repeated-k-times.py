class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        if k>len(s):
            return ''

        ans = ''

        d = defaultdict(int)
        for c in s:
            d[c] += 1

        sd = set()
        for c,cnt in d.items():
            if cnt >= k:
                sd.add(c)

        l = list(sd)
        l.sort(reverse=True)

        mxlen = len(s)//k

        # print(f"test {max('tc','let')}")

        def proc(ss):
            # print(f"proc {ss}")
            i = 0
            for c in s:
                if c == ss[i%len(ss)]:
                    i += 1
            if i//len(ss) >= k:
                # print(f"hit {ss}")
                return ss
            return None
                

        def dfs(i,ss,size):
            nonlocal ans
            if ans:
                return
            if i == size:
                if ss:
                    ts = proc(ss)
                    if ts:
                        ans = ts
                return

            for c in l:
                if d[c] >= k:
                    d[c] -= k
                    dfs(i+1,ss+c,size)
                    d[c] += k

        for size in range(mxlen,0,-1):
            dfs(0,'',size)

        return ans

        

        