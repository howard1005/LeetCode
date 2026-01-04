class Solution:
    pd = set()
    pl = []
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        if not self.pd:
            pd = set(range(2,100001))
            for i in range(2,100001):
                if i not in pd:
                    continue
                pd -= set(range(i*2,100001,i))
            for e in pd:
                self.pd.add(e)
                self.pl.append(e)
            self.pl.sort()

            # print(self.pl)

        def divp(n):
            # d = defaultdict(int)
            # for p in self.p:
            #     if p*p > n:
            #         break
            #     if n%p == 0:
            #         n //= p
            #         d[p] += 1

            # ret = [1]
            # cnt = 1
            # for _,c in d.items():
            #     cnt *= c
            # cnt += 2

            # return True if cnt == 4 else False
            ret = []

            i = 1
            while i*i<=n:
                if n%i == 0:
                    ret.append(i)
                    if i != n//i:
                        ret.append(n//i)
                i += 1

            return ret


        for n in nums:
            l = divp(n)
            # print(l)
            if len(l) == 4:
                ans += sum(l)

        

        

        

        return ans