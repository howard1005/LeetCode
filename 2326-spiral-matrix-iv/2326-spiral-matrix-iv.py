# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dy,dx = [-1,0,1,0],[0,1,0,-1]
        
        mp = [[-1 for _ in range(n)] for _ in range(m)]

        y,x = 0,0
        di = 1
        h = head
        while h:
            mp[y][x] = h.val
            if not h.next:
                break
            ny,nx = y+dy[di],x+dx[di]
            if ny<0 or nx<0 or ny>=m or nx>=n or mp[ny][nx]!=-1:
                di = (di+1)%4
                continue
            y,x = ny,nx
            h = h.next

        return mp