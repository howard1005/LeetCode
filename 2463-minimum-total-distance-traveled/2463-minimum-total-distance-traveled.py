class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        robot.sort()
        factory.sort()

        dp = {}

        def dfs(i,j,k):
            if i == len(robot):
                return 0

            if (i,j,k) in dp:
                return dp[(i,j,k)]
            ret = inf

            if k:
                ret = min(ret,dfs(i+1,j,k-1)+abs(robot[i]-factory[j][0]))
            if j+1 < len(factory):
                ret = min(ret,dfs(i,j+1,factory[j+1][1]))

            dp[(i,j,k)] = ret

            return ret

        return dfs(0,0,factory[0][1])
            