class Solution:
    def canChange(self, start: str, target: str) -> bool:
        


        cnt = 0
        for i in range(len(target)):
            c1,c2 = start[i],target[i]
            
            if c1 == 'L':
                if cnt:
                    return False
            elif c1 == 'R':
                cnt += 1

            if c2 == 'R':
                if cnt == 0:
                    return False
                cnt -= 1
            elif c2 == 'L':
                if cnt:
                    return False
        if cnt:
            return False


        cnt = 0
        for i in range(len(target)-1,-1,-1):
            c1,c2 = start[i],target[i]
            
            if c1 == 'R':
                if cnt:
                    return False
            elif c1 == 'L':
                cnt += 1

            if c2 == 'L':
                if cnt == 0:
                    return False
                cnt -= 1
            elif c2 == 'R':
                if cnt:
                    return False

        if cnt:
            return False

        return True