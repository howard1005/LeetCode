class Solution:
    def longestPalindrome(self, s: str) -> str:        
        def get_max(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return [i+1,j]
        ans = [0,0]
        for i in range(len(s)):
            ret = get_max(i,i)
            if ret[1]-ret[0]>ans[1]-ans[0]:
                ans = ret
            if i+1<len(s) and s[i]==s[i+1]:
                ret = get_max(i,i+1)
                if ret[1]-ret[0]>ans[1]-ans[0]:
                    ans = ret
        return s[ans[0]:ans[1]]