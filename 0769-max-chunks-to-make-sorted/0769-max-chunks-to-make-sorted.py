class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0

        expected = list(sorted(arr))

        def valid(l):
            rl = []
            for ll in l:
                rl.extend(ll)
            
            return rl == expected

        def dfs(i,l,tl):
            nonlocal ans
            cl,ctl = l[:], tl[:]
            if i == len(arr):
                if ctl:
                    ctl.sort()
                    cl.append(ctl)
                # print(cl)
                if valid(cl):
                    ans = max(ans,len(cl))
                return

            ctl.append(arr[i])
            dfs(i+1,cl,ctl)
            ctl.sort()
            dfs(i+1,cl+[ctl],[])

        dfs(0,[],[])

        return ans