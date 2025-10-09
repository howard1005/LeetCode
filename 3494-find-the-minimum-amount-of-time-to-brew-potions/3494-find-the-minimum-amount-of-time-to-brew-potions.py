class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        tl = [0 for _ in range(len(skill))]
        for m in mana:
            # print(m,tl)

            cum = 0
            st = -1
            for t,s in zip(tl,skill):
                st = max(st,t-cum)
                cum += s*m

            l = []
            for s in skill:
                st += s*m
                l.append(st)
            tl = l

            # print(m,tl)

        ans = tl[-1]

        return ans
            