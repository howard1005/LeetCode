class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        
        l = list(strs[0])
        for s in strs[1:]:
            for i in range(len(l)):
                if l[i] == '':
                    continue
                if s[i] < l[i]:
                    l[i] = ''
                    ans += 1
                else:
                    l[i] = s[i]
            
        return ans