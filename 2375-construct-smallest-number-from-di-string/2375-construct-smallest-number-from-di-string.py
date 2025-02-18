class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = ''

        def dfs(i,s,vis):
            nonlocal ans
            if i == len(pattern)+1:
                ans = s
                return True
            if i == 0:
                for n in range(1,10):
                    if n in vis:
                        continue
                    vis.add(n)
                    if dfs(i+1,s+str(n),vis):
                        return True
                    vis.remove(n)
            else:
                p = pattern[i-1]
                last = int(s[-1])
                if p == 'I':
                    for n in range(last+1,10):
                        if n in vis:
                            continue
                        vis.add(n)
                        if dfs(i+1,s+str(n),vis):
                            return True
                        vis.remove(n)
                else:
                    for n in range(last-1,0,-1):
                        if n in vis:
                            continue
                        vis.add(n)
                        if dfs(i+1,s+str(n),vis):
                            return True
                        vis.remove(n)
            return 
        
        dfs(0,'',set())

        return ans
