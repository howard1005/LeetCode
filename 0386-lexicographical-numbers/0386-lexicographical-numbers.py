class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l = [i for i in range(1,n+1)]
        l.sort(key=lambda x: str(x))
        return l

        