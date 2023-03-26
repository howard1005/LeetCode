class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        ans = []
        
        l = [0]*n
        i = rounds[0]-1
        l[i] += 1
        for r in rounds[1:]:
            while i != r-1:
                i = (i+1)%n
                l[i] += 1
        mx = max(l)
        for i,cnt in enumerate(l):
            if cnt == mx:
                ans.append(i+1)
        
        return ans