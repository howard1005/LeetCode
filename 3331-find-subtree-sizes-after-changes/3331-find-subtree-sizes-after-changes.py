class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        
        ed = defaultdict(list)
        for i,p in enumerate(parent):
            ed[p].append(i)

        def dfs(i,vis):
            c = s[i]
            if vis[c]:
                newp = vis[c][-1]
                parent[i] = newp
            vis[c].append(i)
            for ni in ed[i]:
                dfs(ni,vis)
            vis[c].pop()

        dfs(0,defaultdict(list))

        ans = [0 for _ in range(len(parent))]

        ned = defaultdict(list)
        for i,p in enumerate(parent):
            ned[p].append(i)

        def dfs2(i):
            ret = 1
            for ni in ned[i]:
                ret += dfs2(ni)
            ans[i] = ret
            return ret

        dfs2(0)

        return ans
