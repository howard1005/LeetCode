class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        def incre_c(c):
            return chr((ord(c)-ord('a')+1)%26 + ord('a'))

        i,j = 0,0
        while i<len(str1) and j<len(str2):
            c1,c2 = str1[i],str2[j]
            print(c1,c2)
            if c1 == c2 or incre_c(c1) == c2:
                i += 1
                j += 1
            else:
                i += 1
        
        return True if j == len(str2) else False