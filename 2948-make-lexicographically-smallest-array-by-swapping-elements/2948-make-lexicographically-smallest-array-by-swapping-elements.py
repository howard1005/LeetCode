class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ans = [0 for _ in range(len(nums))]

        l = list(sorted([(n,i) for i,n in enumerate(nums)]))

        ll = []
        tl = [l[0]]
        for i in range(1,len(l)):
            if abs(l[i-1][0]-l[i][0]) <= limit:
                tl.append(l[i])
            else:
                ll.append(tl)
                tl = [l[i]]
        ll.append(tl)

        for sl in ll:
            il = list(sorted([i for n,i in sl]))
            for i,(n,_) in zip(il,sl):
                ans[i] = n

        return ans