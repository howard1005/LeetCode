class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        
        def proc(t,cnt):
            nonlocal ans
            j = 0
            for i in range(len(answerKey)):
                if answerKey[i] != t:
                    while cnt <= 0:
                        if answerKey[j] != t:
                            cnt += 1
                        j += 1
                    cnt -= 1
                ans = max(ans,i-j+1)
                
        proc('T',k)
        proc('F',k)
                
        return ans