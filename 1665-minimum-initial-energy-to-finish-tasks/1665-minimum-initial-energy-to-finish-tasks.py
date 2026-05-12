class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = inf

        tasks.sort(key=lambda x: x[0]-x[1])
        # print(tasks)

        def valid(e):
            # print(f"\n==========\n{e}")
            st = []
            for a,m in tasks:
                # print(a,m,st,e)
                # while st and st[-1][0] <= a:
                #     ta,tm = st.pop()
                #     if e < tm:
                #         print("f1")
                #         return False
                #     e -= ta
                st.append((a,m))
            # print("remain", st)
            for a,m in st:
                # print("r",a,m,e)
                if e < m:
                    # print("f2")
                    return False
                e -= a
            # print(e>=0)
            return e>=0

        lo,hi = 0,1000000000
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1

        return ans

