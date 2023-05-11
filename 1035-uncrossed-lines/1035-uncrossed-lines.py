from bisect import bisect_left


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        
        d = defaultdict(list)
        for i,num in enumerate(nums2):
            d[num].append(i)
            
        for i in range(len(nums1)-1,-1,-1):
            for j in range(len(nums2)-1,-1,-1):
                num = nums1[i]
                if num in d:
                    l = d[num]
                    k = bisect_left(l,j)
                    if len(l) != k:
                        ik = l[k]
                        dp[i][j] = max(dp[i][j], dp[i+1][ik+1]+1)
                dp[i][j] = max(dp[i][j], dp[i+1][j])
        
        return dp[0][0]