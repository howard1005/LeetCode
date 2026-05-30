from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        ans = []

        MAX = max(q[1] for q in queries)

        exp = 0
        while (1 << exp) < MAX + 1:
            exp += 1
        
        tree = [0 for _ in range((1 << (1 + exp)))]
        lazy = [0 for _ in range((1 << (1 + exp)))]

        def propagation(i):
            if lazy[i] == 0:
                return
            if 2 * i < len(lazy):
                store(2 * i, lazy[i])
            if 2 * i + 1 < len(lazy):
                store(2 * i + 1, lazy[i])
            lazy[i] = 0

        def flush(i):
            propagation(i)

        def store(i, v):
            tree[i] += v
            lazy[i] += v
        
        def query(us, ue, i=1, s=0, e=(1 << exp) - 1):
            if us > ue or ue < s or e < us:
                return -1

            if us <= s and e <= ue:
                return tree[i]

            flush(i)

            mi = (s + e) // 2
            l = query(us, ue, i * 2, s, mi)
            r = query(us, ue, i * 2 + 1, mi + 1, e)

            return max(l, r)

        def update(us, ue, uv, i=1, s=0, e=(1 << exp) - 1):
            if us > ue or ue < s or e < us:
                return

            if us <= s and e <= ue:
                store(i, uv)
                return

            flush(i)

            mi = (s + e) // 2
            update(us, ue, uv, i * 2, s, mi)
            update(us, ue, uv, i * 2 + 1, mi + 1, e)

            tree[i] = max(tree[i * 2], tree[i * 2 + 1])

        for i in range(MAX):
            update(i, i, MAX - i + 1)
        
        sl = SortedList()
        sl.add(0)
        sl.add(MAX + 1)

        for q in queries:
            if q[0] == 1:
                x = q[1]
                i = sl.bisect_left(x)
                update(sl[i - 1], x - 1, -(sl[i] - x))
                sl.add(x)

            if q[0] == 2:
                x, sz = q[1], q[2]
                i = sl.bisect_right(x)
                p = sl[i - 1]

                v = query(0, p - 1)
                v = max(v, x - p)

                ans.append(v >= sz)

        return ans