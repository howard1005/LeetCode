class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        e1,e2 = [s1[i] for i in range(0,len(s1),2)],[s2[i] for i in range(0,len(s2),2)]
        o1,o2 = [s1[i] for i in range(1,len(s1),2)],[s2[i] for i in range(1,len(s2),2)]
        e1.sort(),e2.sort()
        o1.sort(),o2.sort()

        return e1==e2 and o1==o2