class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        d = {}
        for n in arr:
            d[n] = 1
        m = 1
        while k and m <= 2000:
            if m not in d:
                k -= 1
            m += 1
        return m-1