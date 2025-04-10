class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        start,finish = str(start),str(finish)
        if int(finish) < int(s):
            return 0

        size = len(finish)

        if size == len(s):
            if int(start) > int(s):
                return 0
            return 1

        l1 = [0 for _ in range(size)]
        l2 = [0 for _ in range(size)]

        for i in range(size-1,-1,-1):
            j = size-i
            if j <= len(start):
                l1[i] = int(start[-j])
        
        for i in range(size-1,-1,-1):
            j = size-i
            if j <= len(finish):
                l2[i] = int(finish[-j])

        free = size - len(s)

        p1,p2 = l1[:free],l2[:free]
        t1,t2 = l1[free:],l2[free:]
        # print(free,p1,p2,t1,t2)

        tn1 = int(''.join([str(n) for n in t1]))
        tn2 = int(''.join([str(n) for n in t2]))

        @cache
        def dfs(i,high_fit,low_fit):
            if i == len(p1):
                if high_fit:
                    if int(s) > tn2:
                        return 0
                if low_fit:
                    if int(s) < tn1:
                        return 0
                return 1

            high = min(p2[i],limit) if high_fit else limit
            low = p1[i] if low_fit else 0
            # print(i,high_fit,low_fit,high,low)
            if low > limit:
                return 0

            ret = 0
            for n in range(low,high+1):
                nhigh_fit = 1 if high_fit and p2[i] == n else 0
                nlow_fit = 1 if low_fit and p1[i] == n else 0
                ret += dfs(i+1,nhigh_fit,nlow_fit)
            return ret

        ans = dfs(0,1,1)

        return ans