class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        
        l1 = [0 for _ in range(len(boxes))]
        l2 = [0 for _ in range(len(boxes))]

        cnt = 0
        for i in range(len(boxes)):
            l1[i] = cnt + (l1[i-1] if i else 0)
            cnt += int(boxes[i])
            
        cnt = 0
        for i in range(len(boxes)-1,-1,-1):
            l2[i] = cnt + (l2[i+1] if i+1<len(l2) else 0)
            cnt += int(boxes[i])

        for i in range(len(boxes)):
            ans.append(l1[i]+l2[i])

        return ans