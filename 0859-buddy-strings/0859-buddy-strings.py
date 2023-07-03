class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        d1,d2 = [],[]
        for c1,c2 in zip(s,goal):
            if c1 != c2:
                d1.append(c1)
                d2.append(c2)
        d1.sort()
        d2.sort()
        # print(d1,d2)
        if not d1 and len(set(s)) != len(s):
            return True
        elif len(d1) == 2 and d1 == d2:
            return True
        return False
                