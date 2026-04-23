class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]

        d = defaultdict(list)
        for i,n in enumerate(nums):
            d[n].append(i)
        for _,l in d.items():
            tot = sum(l)
            cum = 0
            cnt = 0
            for i in l:
                ans[i] = tot-cum*2-i*(len(l)-cnt)+cnt*i
                cum += i
                cnt += 1

        return ans