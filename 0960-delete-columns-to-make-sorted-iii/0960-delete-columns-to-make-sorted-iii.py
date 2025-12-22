class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        
        n,m = len(strs),len(strs[0])

        ed = defaultdict(set)

        for i in range(m):
            for j in range(i+1,m):
                flag = True
                for s in strs:
                    if s[i] <= s[j]:
                        pass
                    else:
                        flag = False
                        break
                if flag:
                    ed[i].add(j)
        
        l = [1 for _ in range(m)]
        for i in range(m):
            for j in ed[i]:
                l[j] = max(l[j],l[i]+1)

        ans = m-max(l)

        return ans
                    