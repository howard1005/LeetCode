class Solution:
    def strangePrinter(self, s: str) -> int:
        ans = 0
        
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        
        
        # 첫번째인 i는 이미 print한거라고 잡은거임
        # i번째 문자는 이미출력이 j번째까지 되어 있을때 최소프린트횟수
        def dfs(i,j):
            if i>=j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = inf
            
            c = s[i]
            
            dp[i][j] = dfs(i+1,j)+1 # i+1 번째 문자를 출력하고 나아간다.(i랑 같으면 넘어가도 되긴하지만 그건 어차피 아래 for문에서 처리가 되는거다.)
            for k in range(i,j+1):
                if s[k] == c:
                    dp[i][j] = min(dp[i][j],dfs(i,k-1)+dfs(k,j))
            
            
            
            return dp[i][j]
        
    
        
        ans = dfs(0,len(s)-1)+1 

        # for r in dp:
        #     print(r)
        
        return ans
        
        
#         dp = {}
        
#         d = defaultdict(list)
        
#         def dfs(i,ss):
#             if i >= len(s):
#                 return 0
            
#             # print(i,ss)
            
#             ss = tuple(ss)
            
#             if ss and s[i] == ss[0]:
#                 return dfs(i+1,ss[1:])
            
#             if (i,ss) in dp:
#                 return dp[(i,ss)]
#             dp[(i,ss)] = inf
            
            
#             # c = s[i]
#             # nss = ''
#             # for j in range(i+1,len(s)):
#             #     k = j-i
#             #     if k < len(ss) and s[j] == ss[k]:
#             #         dp[(i,ss)] = min(dp[(i,ss)],1+dfs(i+1,nss+ss[1+len(nss):]))
#             #     nss += c
                    
            
            
#             # if i in d:
#             #     for nss in d[i]:
#             #         dp[(i,ss)] = min(dp[(i,ss)],1+dfs(i+1,nss+ss[1+len(nss):]))
#             #     return dp[(i,ss)]
            
#             c = s[i]
#             nss = list(ss[1:])
#             nssi = 0
#             flag = 1
#             for j in range(i+1,len(s)):
#                 if flag and s[j] != c:
#                     flag = 0
#                     # d[i].append(nss)
#                     dp[(i,ss)] = min(dp[(i,ss)],1+dfs(i+1,nss))
#                 elif s[j] == c:
#                     flag = 1
#                 nss[nssi] = c
#                 nssi += 1
#             if s[-1] == c:
#                 # d[i].append(nss)
#                 dp[(i,ss)] = min(dp[(i,ss)],1+dfs(i+1,nss))
            
#             return dp[(i,ss)]
                
#         ans = dfs(0,['']*len(s))
        
#         print(len(dp))
#         # print(d)
        
#         return ans
        
        
        
        
        
        
        
#         dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        
#         def dfs(i,j):
#             if dp[i][j] != -1:
#                 return dp[i][j]
#             dp[i][j] = inf
            
#             c = s[i]
            
#             cum = 1
#             ii = i-1
#             for k in range(i,j+1):
#                 if s[k] == c:
#                     if k-ii > 1:
#                         dp[i][j] = min(dp[i][j],cum+dfs(ii+1,j))
#                         cum += dfs(ii+1,k-1)
#                     ii = k
#             if ii != j:
#                 cum += dfs(ii+1,j)
#             dp[i][j] = min(dp[i][j],cum)
            
#             return dp[i][j]
        
#         ans = dfs(0,len(s)-1)
        
#         print(dp)
        
#         return ans