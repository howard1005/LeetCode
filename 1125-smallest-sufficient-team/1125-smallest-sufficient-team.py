class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:        
        d = {}
        for i,skill in enumerate(req_skills):
            d[skill] = i
            
        pl = []
        for p in people:
            m = 0
            for skill in p:
                m |= (1<<d[skill])
            pl.append(m)
            
        dp = [[(-1,()) for _ in range(1<<len(d))] for _ in range(len(pl))]
        
        def dfs(i,m):
            if i >= len(pl):
                if m == (1<<len(d))-1:
                    return (0,())
                return (inf,())
            
            if dp[i][m][0] != -1:
                return dp[i][m]
            dp[i][m] = (inf,())
            
            size,t = dfs(i+1,m)
            if size < dp[i][m][0]:
                dp[i][m] = (size,t)
                
            size,t = dfs(i+1,(m|(pl[i])))
            if size+1 < dp[i][m][0]:
                dp[i][m] = (size+1,t+(i,))
            
            return dp[i][m]
        
        return dfs(0,0)[1]