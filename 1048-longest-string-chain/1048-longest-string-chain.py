from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d = defaultdict(list)
        for i in range(len(words)):
            d[words[i]].append(i)
        
        child = [[] for _ in range(len(words))]
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                pre_word = word[:j] + word[j+1:]
                for idx in d[pre_word]:
                    child[i].append(idx)
        
        #print(child)

        vis = [0 for _ in range(len(words))]
        def dfs(i):
            if vis[i]: return vis[i]
            if not child[i]:
                return 1
            for idx in child[i]:
                vis[i] = max(vis[i],1+dfs(idx))
            return vis[i]
        
        
        ans = 0
        for i in range(len(child)):
            ans = max(ans,dfs(i))
            
        #print(vis)
        
        return ans
            
                
                
        
        