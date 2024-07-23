class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        l = sorted([(cnt,-n) for n,cnt in d.items()])

        retl = []

        for cnt,n in l:
            for _ in range(cnt):
                retl.append(-n)

        return retl