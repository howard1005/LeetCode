class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = inf

        for i,w in enumerate(words):
            if w == target:
                dis = abs(startIndex-i)
                ans = min(ans,dis,len(words)-dis)
                
        return ans if ans != inf else -1