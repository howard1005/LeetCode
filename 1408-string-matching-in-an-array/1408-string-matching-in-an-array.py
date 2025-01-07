class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []

        for i,w1 in enumerate(words):
            for j,w2 in enumerate(words):
                if i == j:
                    continue
                if w1 in w2:
                    ans.append(w1)
                    break

        return ans