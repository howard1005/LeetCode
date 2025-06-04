class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        ans = ''

        mxlen = len(word)-(numFriends-1)
        # print(mxlen)

        for i in range(len(word)):
            ans = max(ans,word[i:i+mxlen])
            
        return ans