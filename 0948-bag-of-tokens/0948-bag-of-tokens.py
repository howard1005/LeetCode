class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        
        tokens.sort()
        score = 0
        i,j = 0,len(tokens)-1
        flag = 1
        while flag:
            flag = 0
            while i<=j and tokens[i]<=power:
                power -= tokens[i]
                score += 1
                i += 1
                flag = 1
            ans = max(ans, score)
            if i<=j and score:
                power += tokens[j]
                score -= 1
                j -= 1
                flag = 1
        
        return ans