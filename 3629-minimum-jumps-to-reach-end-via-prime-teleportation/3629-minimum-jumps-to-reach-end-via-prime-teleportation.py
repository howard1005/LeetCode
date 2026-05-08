class Solution:
    pd = set()
    ppd = defaultdict(list)
    def minJumps(self, nums: List[int]) -> int:
        ans = 0

        if not self.pd:
            pd = set(range(2,1000001))
            for n in range(2,1000001):
                if n not in pd:
                    continue
                pd -= set(range(n*2,1000001,n))
            self.pd |= pd
            for p in pd:
                for pp in range(p,1000001,p):
                    self.ppd[p].append(pp)
        # print(len(self.pd))

        ed = defaultdict(set)
        nd = defaultdict(set)
        d = defaultdict(list)

        for i,n in enumerate(nums):
            d[n].append(i)

        for i,n in enumerate(nums):
            if i-1>=0:
                ed[i].add(i-1)
            if i+1<len(nums):
                ed[i].add(i+1)
            if n in self.pd and n not in nd:
                for m in self.ppd[n]:
                    if m in d:
                        for j in d[m]:
                            nd[n].add(j)
        # print(ed)
        
        vis = {0}
        nvis = set()
        dq = deque([(0,0)])
        while dq:
            i,c = dq.popleft()
            # print(i,c)
            if i == len(nums)-1:
                ans = c
                break
            for ni in ed[i]:
                if ni in vis:
                    continue
                vis.add(ni)
                dq.append((ni,c+1))
            if nums[i] not in nvis:
                nvis.add(nums[i])
                for ni in nd[nums[i]]:
                    if ni in vis:
                        continue
                    vis.add(ni)
                    dq.append((ni,c+1))
            

        return ans