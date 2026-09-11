class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = 0

        sd = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if i == k or j == k:
                        continue
                    n = digits[i]*100 + digits[j]*10 + digits[k]
                    if n//100 == 0:
                        continue
                    if n%2:
                        continue
                    sd.add(n)

        ans = len(sd)

        return ans