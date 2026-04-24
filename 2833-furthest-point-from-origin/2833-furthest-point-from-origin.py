class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ans = 0

        cnt = 0
        dis = 0
        for c in moves:
            if c == '_':
                cnt += 1
            if c == 'R':
                dis += 1
            if c == 'L':
                dis -= 1
        if dis > 0:
            ans = dis + cnt
        else:
            ans = cnt - dis

        return ans