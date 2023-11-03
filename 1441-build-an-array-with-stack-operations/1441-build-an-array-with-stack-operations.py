class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        
        stream = [i for i in range(n,0,-1)]
        for t in target:
            while stream and stream[-1] != t:
                stream.pop()
                ans.extend(["Push","Pop"])
            stream.pop()
            ans.append("Push")
            
        return ans