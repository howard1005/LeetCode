class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        ans = []

        
        dp = [0 for _ in range(len(word1))]

        dp[-1] = 1 if word1[-1] == word2[-1] else 0

        for i in range(len(dp)-2,-1,-1):
            dp[i] = dp[i+1]
            if dp[i+1]<len(word2) and word1[i] == word2[len(word2)-1-dp[i+1]]:
                dp[i] += 1
        
        # print(dp)

        i,j = 0,0
        r = len(word2)
        while i<len(word1)-1 and j<len(word2):
            if word1[i] != word2[j] and r-1 <= dp[i+1]:
                ans.append(i)
                i += 1
                j += 1
                while i<len(word1) and len(ans) < len(word2):
                    if word1[i] == word2[j]:
                        ans.append(i)
                        j += 1
                    i += 1
                break
            if word1[i] == word2[j]:
                ans.append(i)
                r -=1
                j += 1
            i += 1
            

        return ans if len(ans) == len(word2) else []