class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return list(map(lambda x: x[1],sorted([(sum(r),i)for i,r in enumerate(mat)])[:k]))