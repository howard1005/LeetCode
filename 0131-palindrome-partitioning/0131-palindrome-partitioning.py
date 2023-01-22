class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def chk_pand(ss):
            i,j = 0,len(ss)-1
            while i <= j:
                if ss[i] != ss[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def dfs(i,l):
            if i == len(s):
                ans.append(l)
            for j in range(i+1,len(s)+1):
                if chk_pand(s[i:j]):
                    dfs(j,l+[s[i:j]])
        
        dfs(0,[])
        
        return ans