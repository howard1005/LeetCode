class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        def valid(offset):
            for i in range(len(s)):
                if s[i] != goal[(i+offset)%len(goal)]:
                    return False
            return True


        for i in range(len(s)):
            if valid(i):
                return True
        
        return False
