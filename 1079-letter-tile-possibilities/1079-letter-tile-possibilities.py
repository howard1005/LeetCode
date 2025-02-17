class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sd = set()

        def dfs(s,vis,size):
            if len(vis) == size:
                sd.add(s)
                return
            for i in range(len(tiles)):
                if i in vis:
                    continue
                vis.add(i)
                dfs(s+tiles[i],vis,size)
                vis.remove(i)
        for size in range(1,len(tiles)+1):
            dfs('',set(),size)

        return len(sd)