class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []

        for q in queries:
            for w in dictionary:
                cnt = 0
                for i in range(len(q)):
                    if q[i] != w[i]:
                        cnt += 1
                if cnt <= 2:
                    ans.append(q)
                    break
        
        return ans