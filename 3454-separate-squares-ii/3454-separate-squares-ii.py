from typing import List
from collections import defaultdict

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # (선택) 같은 (x,y)에서 작은 정사각형은 큰 정사각형에 포함되므로 제거 가능
        d = defaultdict(int)
        for x, y, le in squares:
            if le > d[(x, y)]:
                d[(x, y)] = le

        events = []   # (y, type(+1 start / -1 end), x1, x2)
        xs = set()

        for (x, y), le in d.items():
            x1, x2 = x, x + le
            y1, y2 = y, y + le
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))
            xs.add(x1); xs.add(x2)

        events.sort()
        xs = sorted(xs)

        # x 세그먼트 개수 = len(xs) - 1
        m = len(xs) - 1
        if m <= 0:
            # 정사각형이 하나라도 있으면 m>=1이지만, 안전 처리
            return float(events[0][0]) if events else 0.0

        xid = {v: i for i, v in enumerate(xs)}

        # 세그트리: cnt가 0보다 크면 해당 구간 전체가 덮임
        cnt = [0] * (4 * m)
        covered = [0.0] * (4 * m)

        def pull(idx: int, l: int, r: int):
            if cnt[idx] > 0:
                covered[idx] = xs[r + 1] - xs[l]
            elif l == r:
                covered[idx] = 0.0
            else:
                covered[idx] = covered[idx * 2] + covered[idx * 2 + 1]

        def update(idx: int, l: int, r: int, ql: int, qr: int, delta: int):
            if qr < l or r < ql:
                return
            if ql <= l and r <= qr:
                cnt[idx] += delta
                pull(idx, l, r)
                return
            mid = (l + r) // 2
            update(idx * 2, l, mid, ql, qr, delta)
            update(idx * 2 + 1, mid + 1, r, ql, qr, delta)
            pull(idx, l, r)

        def reset_tree():
            # 2번 sweep 하려고 트리 초기화
            for i in range(len(cnt)):
                cnt[i] = 0
                covered[i] = 0.0

        def sweep(target_area=None):
            """
            target_area=None: 전체 유니온 면적 반환
            target_area=half: 누적 면적이 half 되는 y를 반환
            """
            i = 0
            prev_y = events[0][0]
            acc = 0.0

            while i < len(events):
                y = events[i][0]
                dy = y - prev_y
                if dy > 0:
                    width = covered[1]
                    slab = width * dy

                    if target_area is not None and acc + slab >= target_area:
                        # 이 슬랩 내부에서 해를 찾는다.
                        # width==0이면 슬랩 면적이 0이라 여기서 걸릴 일이 없음.
                        return prev_y + (target_area - acc) / width

                    acc += slab
                    prev_y = y

                # y에서 발생하는 모든 이벤트 적용
                while i < len(events) and events[i][0] == y:
                    _, typ, x1, x2 = events[i]
                    l = xid[x1]
                    r = xid[x2] - 1   # [x1, x2) 이므로 세그먼트 인덱스는 x2-1까지
                    if l <= r:
                        update(1, 0, m - 1, l, r, typ)
                    i += 1

            return acc

        total = sweep(target_area=None)
        half = total / 2.0

        reset_tree()
        ans = sweep(target_area=half)
        return float(ans)
