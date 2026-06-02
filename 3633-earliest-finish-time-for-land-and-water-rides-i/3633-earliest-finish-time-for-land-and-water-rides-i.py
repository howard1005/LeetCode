class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = inf

        for la,lb in zip(landStartTime,landDuration):
            for wa,wb in zip(waterStartTime,waterDuration):
                a1,b1 = la,la+lb
                a2,b2 = wa,wa+wb
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