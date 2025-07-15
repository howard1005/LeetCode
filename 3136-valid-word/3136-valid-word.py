class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        def isDUL(w):
            for c in w:
                if c in '@#$':
                    return False
            return True

        if not isDUL(word):
            return False 
                
        def isV(w):
            for c in w:
                if c in 'aeiouAEIOU':
                    return True
            return False
        
        if not isV(word):
            return False

        def isC(w):
            for c in w:
                if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                    return True
            return False

        if not isC(word):
            return False
            

        return True