class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        
        d = {}
        f = fruits[0]
        prev = -1
        for i,t in enumerate(fruits):
            if prev != t:
                if t in d:
                    f = prev
                    d[t][0] = i
                elif len(d) == 2:
                    del d[f]
                    (f,) = d.keys()
                    d[f][1] = d[f][0]
                    d[t] = [i,i]
                else:
                    d[t] = [i,i]
                prev = t
            ans = max(ans, i-min(map(lambda x:x[1], d.values()))+1)
                
        return ans