class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        d = defaultdict(set)

        for s in allowed:
            k,v = s[:2],s[2]
            d[k].add(v)

        def dfs(i,fs,nfs):
            # print(i,fs,nfs)
            if i == len(fs)-1:
                if i == 0:
                    return True
                if dfs(0,nfs,''):
                    return True
            k = fs[i:i+2]
            for c in d[k]:
                if dfs(i+1,fs,nfs+c):
                    return True
            return False

        ans = dfs(0,bottom,'')

        return ans
            
            