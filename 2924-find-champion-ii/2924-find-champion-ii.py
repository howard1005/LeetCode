class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inds = defaultdict(int)

        for a,b in edges:
            inds[b] += 1

        ansl = []

        for i in range(n):
            if not inds[i]:
                ansl.append(i)

        return ansl[0] if len(ansl) == 1 else -1