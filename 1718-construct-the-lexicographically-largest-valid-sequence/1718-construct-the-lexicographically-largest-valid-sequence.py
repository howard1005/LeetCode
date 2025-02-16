class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ansd = set()

        size = n*2-1
        
        def dfs(i,l,vis):
            if i == len(l):
                ansd.add(tuple(l))
                return True
            if l[i]:
                if dfs(i+1,l,vis):
                    return True
                return False
            for j in range(n,0,-1):
                if j in vis:
                    continue
                if j == 1:
                    l[i] = j
                    vis.add(j)
                    if dfs(i+1,l,vis):
                        return True
                    l[i] = 0
                    vis.remove(j)
                elif j+i < len(l) and l[i] == 0 and l[j+i] == 0:
                    l[i] = l[j+i] = j
                    vis.add(j)
                    if dfs(i+1,l,vis):
                        return True
                    l[i] = l[j+i] = 0
                    vis.remove(j)

        dfs(0,[0 for _ in range(size)],set())

        return max(ansd)