class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(l):
            if len(l) == 1:
                if int(l[0]) == 24:
                    return True
                return False

            for i in range(len(l)):
                for j in range(i+1,len(l)):
                    nl = l[:]
                    a,b = nl[i],nl[j]
                    del nl[j]
                    del nl[i]

                    if dfs(nl+[a+b]):
                        return True
                    if dfs(nl+[a-b]):
                        return True
                    if dfs(nl+[b-a]):
                        return True
                    if dfs(nl+[a*b]):
                        return True
                    if b!=0 and dfs(nl+[a/b]):
                        return True
                    if a!=0 and dfs(nl+[b/a]):
                        return True
            
            return False

        ans = dfs(cards)

        return ans

                    
                    