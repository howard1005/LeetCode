class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j != k and i != k:
                        a,b,c = digits[i],digits[j],digits[k]
                        n = a*100 + b*10 + c
                        if n >= 100 and n%2 == 0:
                            ans.add(n)
        ansl = list(ans)    
        ansl.sort()

        return ansl