class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {
            5:0,
            10:0,
            20:0
        }

        for b in bills:
            d[b] += 1
            r = b-5
            if r == 15:
                if d[5] and d[10]:
                    d[5] -= 1
                    d[10] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
            elif r == 10:
                if d[10]:
                    d[10] -= 1
                elif d[5] >= 2:
                    d[5] -= 2
                else:
                    return False
            elif r == 5:
                if d[5]:
                     d[5] -= 1
                else:
                    return False

        return True
                
                
            