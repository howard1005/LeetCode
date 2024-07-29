class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0

        l1 = [0 for _ in range(len(rating))]
        l2 = [0 for _ in range(len(rating))]

        for i in range(len(rating)):
            for j in range(i):
                if rating[j] < rating[i]:
                    l1[i] += 1
                if rating[j] > rating[i]:
                    l2[i] += 1
        
        for i in range(len(rating)):
            for j in range(i):
                if rating[j] < rating[i]:
                    ans += l1[j]
                if rating[j] > rating[i]:
                    ans += l2[j]

        return ans
        