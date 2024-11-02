class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split(" ")
        for i in range(len(l)):
            if l[i][0] != l[i-1][-1]:
                return False

        return True
            