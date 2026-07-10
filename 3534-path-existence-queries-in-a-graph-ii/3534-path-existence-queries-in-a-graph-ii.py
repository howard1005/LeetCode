from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        ans = []

        l = [(i,v) for i,v in enumerate(nums)]
        l.sort(key=lambda x: x[1])

        rd = {}
        for i,(j,_) in enumerate(l):
            rd[j] = i

        # print(l)

        dp = [[] for _ in range(len(l))]

        for i in range(len(l)-1,-1,-1):
            v = l[i][1]
            j = bisect_right(l,v+maxDiff,i+1,len(l),key=lambda x:x[1])-1
            if j>i and j<len(dp):
                dp[i].append(j)
                while len(dp[i])-1<len(dp[j]):
                    dp[i].append(dp[j][len(dp[i])-1])
                    j = dp[i][-1]
        # print(dp)

        for a,b in queries:
            i,j = rd[a],rd[b]
            i,j = min(i,j),max(i,j)
            # print("q",a,b,i,j)

            diff = j-i
            cost = 0
            
            le = len(dp[i])
            for k in range(le-1,-1,-1):
                if k>=len(dp[i]):
                    continue
                if dp[i][k]>j:
                    continue
                i = dp[i][k]
                diff = j-i
                cost += 2**k
                if diff == 0:
                    break
            # print(i,dp[i],diff,cost)
            if diff == 0:
                ans.append(cost)
            elif dp[i] and j<=dp[i][0]:
                ans.append(cost+1)
            else:
                ans.append(-1)                    

        return ans