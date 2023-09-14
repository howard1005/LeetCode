class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        
        d = defaultdict(list)
        
        for i,(a,b) in enumerate(tickets):
            d[a].append((b,i))
        for l in d.values():
            l.sort()
        
        vis = defaultdict(int)
        def dfs(a, depth, l):
            # print(a,depth,l)
            if depth == len(tickets):
                ans.extend(l)
                return True
            for b,i in d[a]:
                if vis[i] == 0:
                    vis[i] = 1
                    l.append(b)
                    if dfs(b,depth+1,l):
                        return True
                    l.pop()
                    vis[i] = 0
            return False
                    
        dfs("JFK",0,["JFK"])
                    
        return ans