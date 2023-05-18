class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set({i for i in range(n)})
        
        for a,b, in edges:
            ans.discard(b)
            
        return ans