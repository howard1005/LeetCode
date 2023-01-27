class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        
        d = set(words)
        
        def chk(s,i):
            sub = ''
            for j in range(i,len(s)):
                sub += s[j]
                if sub in d:
                    if j+1 < len(s):
                        if chk(s,j+1):
                            return True
                    elif i != 0:
                        return True
            return False
        
        for word in words:
            if chk(word,0):
                ans.append(word)
        
        return ans