class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:

        k = k1+k2

        l = []
        for a,b in zip(nums1,nums2):
            l.append(abs(a-b))
        l.sort(reverse=True)

        ans = 0

        n = len(l)
        l.append(0)  # 마지막에는 모든 차이를 0까지 낮춤

        for i in range(n):
            count = i + 1
            t = l[i]

            # 상위 count개를 다음 값의 높이까지 낮추는 비용
            cost = (t - l[i + 1]) * count

            if k >= cost:
                k -= cost
            else:
                # 다음 높이까지 못 내려가면 남은 연산을 고르게 분배
                q, r = divmod(k, count)
                t -= q

                ans = (count - r) * t * t
                ans += r * (t - 1) * (t - 1)
                ans += sum(x * x for x in l[i + 1:n])
                return ans
        return ans 
            