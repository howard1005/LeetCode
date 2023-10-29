import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        ans = math.log(buckets,minutesToTest//minutesToDie+1)
        if ans - int(ans) < 0.00000001:
            return int(ans)
        return math.ceil(ans)