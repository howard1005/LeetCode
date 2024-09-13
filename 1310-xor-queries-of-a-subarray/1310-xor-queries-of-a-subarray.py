class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cuml = [arr[0]]
        for n in arr[1:]:
            cuml.append(cuml[-1]^n)
            
        return [cuml[b]^(cuml[a-1] if a else 0) for a,b in queries]