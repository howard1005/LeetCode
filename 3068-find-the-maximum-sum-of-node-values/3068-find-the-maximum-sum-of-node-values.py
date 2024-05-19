class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        def dfs(p,n):
            ret = [-inf,-inf]

            l = []
            for nn in d[n]:
                if nn == p:
                    continue
                z,o = dfs(n,nn)
                xz = z-nums[nn]+(nums[nn]^k)
                xo = o-(nums[nn]^k)+nums[nn]
                l.append((max(z,o),max(xz,xo)))
            l.sort(key=lambda x: x[0]-x[1])

            cum = 0
            for z,o in l:
                cum += z
            ret[0] = nums[n] + cum
            
            for i,(z,o) in enumerate(l):
                cum += -z+o
                if i%2 == 0:
                    ret[1] = max(ret[1],(nums[n]^k)+cum)
                else:
                    ret[0] = max(ret[0],(nums[n])+cum)
            
            return ret

        return max(dfs(-1,0))

            

