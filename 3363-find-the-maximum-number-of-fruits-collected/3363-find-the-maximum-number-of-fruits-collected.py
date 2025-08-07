class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        ans = 0

        MAX = 10**9

        ch1 = 0
        for i in range(len(fruits)):
            ch1 += fruits[i][i]
            fruits[i][i] = 0

        @cache
        def dfs2(i,j):
            if i == len(fruits)-1:
                return 0 if j == len(fruits) else -MAX
            ret = fruits[i][j]
            for k in range(j-1,j+2):
                if k<0 or k>=len(fruits) or k <= i+1:
                    continue
                ret = max(ret,dfs2(i+1,k)+fruits[i][j])
            return ret

        @cache
        def dfs3(i,j):
            if j == len(fruits)-1:
                return 0 if i == len(fruits) else -MAX
            ret = fruits[i][j]
            for k in range(i-1,i+2):
                if k<0 or k>=len(fruits) or k <= j+1:
                    continue
                ret = max(ret,dfs3(k,j+1)+fruits[i][j])
            # print(f"dfs3 {i},{j},{ret}")
            return ret

        
        ch2 = dfs2(0,len(fruits)-1)
        ch3 = dfs3(len(fruits)-1,0)

        # print(ch1,ch2,ch3)

        ans += ch1 + ch2 + ch3

        return ans

