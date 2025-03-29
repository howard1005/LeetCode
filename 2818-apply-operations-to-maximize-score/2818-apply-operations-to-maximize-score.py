class Solution:
    d = defaultdict(int)
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = 1

        MOD = 1000000007

        d = self.d
        if not d:
            sd = set(range(2,100001))
            for i in range(2,100001):
                if i not in sd:
                    continue
                sd -= set(range(i*2,100001,i))
            l = list(sd)
            l.sort()
            d[1] = 0
            for p in l:
                m = p
                while 100000 >= m:
                    d[m] += 1
                    m += p

        l = [d[n] for n in nums]
        # print(l)
        st = []
        cntd = defaultdict(int)

        for i,score in enumerate(l):
            # print(i,score,st)
            while st and st[-1][1] < score:
                idx,_ = st.pop()
                j = st[-1][0] if st else -1
                cnt = (i-idx)*(idx-j)
                cntd[nums[idx]] += cnt
            st.append((i,score))
        i = len(l)
        while st:
            idx,_ = st.pop()
            j = st[-1][0] if st else -1
            cnt = (i-idx)*(idx-j)
            cntd[nums[idx]] += cnt
        
        # print(cntd)

        def exp(n,x):
            return pow(n, x, MOD)

        nl = list(set(nums))
        nl.sort(reverse=True)
        for n in nl:
            # print(n,cntd[n],k)
            if k >= cntd[n]:
                k -= cntd[n]
                ans = (ans*exp(n,cntd[n]))%MOD
            else:
                ans = (ans*exp(n,k))%MOD
                break

        return ans