import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        # 특정 버킷을 찾아내는것이 아닌 버킷을 찾아낼수 있느냐(분별할 수 있느냐) 가 핵심
        # 총 25개의 버킷(1,2,3...25)이 있을때 각 버킷이 독인 세상이 25개가 존재 한다고 해보자.
        # 그럼에도 각 세상에서는 동일한 방식으로 테스트를 하면, 어떤 세상은 한번만에 찾을 수도 어떤세상은 최악의 경우가 될 수 있다.
        # 문제는 최악의 경우에도 찾을 수 있어야 한다.
        # 테스트를 할때 분기하는것은 돼지의 상태(죽/살) 이다.
        # 즉, 각 분기로 인해 만들어 질 수 있는  모든 경우의 수가 무조건 버킷 갯수 보다는 많아야 뭘 어떻게 하든, 상황이 안좋든 분별을 반드시 할 수 있다는 소리

        
        ans = math.log(buckets,minutesToTest//minutesToDie+1)
        if ans - int(ans) < 0.00000001:
            return int(ans)
        return math.ceil(ans)