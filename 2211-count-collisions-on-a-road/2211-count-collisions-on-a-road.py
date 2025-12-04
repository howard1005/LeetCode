class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0

        rcnt = 0
        flag = False
        for c in directions:
            if c == 'R':
                rcnt += 1
                flag = True
            elif c == 'L':
                if flag:
                    ans += 1
                ans += rcnt
                rcnt = 0
            else:
                ans += rcnt
                rcnt = 0
                flag = True

        return ans
                
                