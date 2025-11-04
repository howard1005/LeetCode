class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i,j = 0,0
        d = defaultdict(int)
        while j<k:
            d[nums[j]] += 1
            j += 1

        ans = []

        while i<len(nums)-k+1:
            l = [(v,k) for k,v in d.items()]
            l.sort(reverse=True)
            cum = 0
            for v,cnt in l[:x]:
                cum += v*cnt
            ans.append(cum)
            d[nums[i]] -= 1
            if j<len(nums):
                d[nums[j]] += 1
            j += 1
            i += 1

        return ans
