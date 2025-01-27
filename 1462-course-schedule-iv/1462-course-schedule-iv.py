class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []

        ed = defaultdict(list)
        inds = defaultdict(int)
        pd = defaultdict(set)

        for a,b in prerequisites:
            ed[a].append(b)
            inds[a]
            inds[b] += 1

        dq = deque()
        for k,v in inds.items():
            if v == 0:
                dq.append(k)

        while dq:
            n = dq.popleft()
            for nn in ed[n]:
                inds[nn] -= 1
                pd[nn].add(n)
                pd[nn].update(pd[n])
                if inds[nn] == 0:
                    dq.append(nn)

        for a,b in queries:
            ans.append(a in pd[b])

        return ans
