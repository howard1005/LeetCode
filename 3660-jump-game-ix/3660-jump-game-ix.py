class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]

        ed = defaultdict(set)

        st = []
        for i,n in enumerate(nums):
            v = n
            while st and st[-1][1] > n:
                j,m = st.pop()
                ed[i].add(j)
                ed[j].add(i)
                v = max(v,m)
            st.append((i,v))
        #     print("after",i,st)
        # print(ed)

        vis = set()
        def bfs(i):
            retv = nums[i]
            retl = []
            vis.add(i)
            dq = deque([i])
            while dq:
                j = dq.popleft()
                retl.append(j)
                for jj in ed[j]:
                    if jj in vis:
                        continue
                    vis.add(jj)
                    dq.append(jj)
                    retv = max(retv,nums[jj])
            return retv,retl

        for i in range(len(nums)):
            if i in vis:
                continue
            v,l = bfs(i)
            for j in l:
                ans[j] = v
            
        return ans