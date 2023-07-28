class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
        
        def dfs(i,j,k):
            if i > j:
                return (0,0)
            
            if dp[i][j] != None:
                return dp[i][j]
            dp[i][j] = ()
            
            t1 = dfs(i+1,j,k^1)
            lt1 = list(t1)
            lt1[k] += nums[i]
            t2 = dfs(i,j-1,k^1)
            lt2 = list(t2)
            lt2[k] += nums[j]

            if lt1[k] < lt2[k]:
                dp[i][j] = tuple(lt2)
            else:
                dp[i][j] = tuple(lt1)

            return dp[i][j]
        
        ret = dfs(0,len(nums)-1,0)

        return ret[0] >= ret[1]
