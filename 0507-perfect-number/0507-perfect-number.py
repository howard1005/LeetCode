class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        
        cum = 1
        i = 2
        while i*i<num:
            if num%i == 0:
                cum += i+num//i
            i += 1
        if i*i == num:
            cum += i
        
        return num == cum