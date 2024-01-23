class Solution:
    def maxLength(self, arr: List[str]) -> int:
        i = 0
        while i < len(arr):
            if len(arr[i]) != len(set(arr[i])):
                del arr[i]
            else:
                i += 1
            
        l = [0 for _ in range(26)]
        d = {}
        
        def dfs(i,cnt,st):
            if i == len(arr):
                return cnt
            if st in d:
                return d[st]
            ret = 0
            s = arr[i]
            flag = 1
            for c in s:
                if l[ord(c)-ord('a')]:
                    flag = 0
            
            ret = max(ret,dfs(i+1,cnt,st))
            if flag:
                for c in s:
                    l[ord(c)-ord('a')] = 1
                ret = max(ret,dfs(i+1,cnt+len(s),st|(1<<i)))
                for c in s:
                    l[ord(c)-ord('a')] = 0
            d[st] = ret
            return ret
        
        return dfs(0,0,0)