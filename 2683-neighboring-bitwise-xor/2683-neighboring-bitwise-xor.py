class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        l = [0 for _ in range(len(derived))]

        for i,b in enumerate(derived):
            if i != len(derived)-1:
                l[i+1] = b^l[i]
            elif l[0] == b^l[i]:
                return True

        l[0] = 1
        for i,b in enumerate(derived):
            if i != len(derived)-1:
                l[i+1] = b^l[i]
            elif l[0] == b^l[i]:
                return True
                
        return False
            