class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = inf

        l1 = [(la,la+lb) for la,lb in zip(landStartTime,landDuration)]
        l2 = [(wa,wa+wb) for wa,wb in zip(waterStartTime,waterDuration)]
        l1.sort(key=lambda x:(x[1],-x[0]))
        l2.sort(key=lambda x:(x[1],-x[0]))

        a1,b1 = l1[0]
        for a2,b2 in l2:
            if b1 <= a2:
                ans = min(ans,b2)
            elif b2 <= a1:
                ans = min(ans,b1)
            else:
                if a1 <= a2:
                    ans = min(ans,b1+b2-a2)
                else:
                    ans = min(ans,b2+b1-a1)

        a1,b1 = l2[0]
        for a2,b2 in l1:
            if b1 <= a2:
                ans = min(ans,b2)
            elif b2 <= a1:
                ans = min(ans,b1)
            else:
                if a1 <= a2:
                    ans = min(ans,b1+b2-a2)
                else:
                    ans = min(ans,b2+b1-a1)

        return ans