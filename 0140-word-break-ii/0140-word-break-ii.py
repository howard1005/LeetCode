class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = set()

        d = set()
        for w in wordDict:
            d.add(w)
        
        def dfs(i,ss,sl):
            if i == len(s):
                if not ss and sl:
                    ans.add(' '.join(sl))
                return
            ss += s[i]
            dfs(i+1,ss,sl)
            if ss in d:
                dfs(i+1,'',sl+[ss])
        
        dfs(0,'',[])

        return ans