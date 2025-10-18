class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        prev = nums[0]-k
        sd = set([nums[0]-k])
        for n in nums[1:]:
            # prev - n < min([-k..k])
            m = prev-n
            if m+1 <= -k:
                prev = n-k
                sd.add(prev)
            elif m >= k:
                sd.add(prev)
            else:
                prev = prev+1
                sd.add(prev)
            # print(f"{n}->{prev}")

        # print(sd)

        ans = len(sd)

        return ans

            