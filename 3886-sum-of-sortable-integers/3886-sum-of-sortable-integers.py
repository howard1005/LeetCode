class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        def check(k):
            prev_max = None

            for i in range(0, n, k):
                block = nums[i:i+k]

                mn = min(block)
                mx = max(block)

                if prev_max is not None and prev_max > mn:
                    return False

                cnt = 0
                for j in range(k):
                    if block[j] > block[(j+1) % k]:
                        cnt += 1
                        if cnt > 1:
                            return False

                prev_max = mx

            return True

        for k in range(1, int(n**0.5) + 1):
            if n % k:
                continue

            if check(k):
                ans += k

            other = n // k

            if other != k and check(other):
                ans += other

        return ans