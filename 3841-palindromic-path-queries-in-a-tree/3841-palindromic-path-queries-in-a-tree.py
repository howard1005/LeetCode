
class Solution:
    def palindromePath(
        self,
        n: int,
        edges: list[list[int]],
        s: str,
        queries: list[str]
    ) -> list[bool]:

        ans = []

        # 1. 트리 생성
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n

        # 2. DFS 순회 순서 생성 (재귀 깊이 문제 방지)
        order = [0]

        for u in order:
            for v in g[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        # 3. 서브트리 크기 및 Heavy Child 계산
        for u in reversed(order):
            max_size = 0

            for v in g[u]:
                if v == parent[u]:
                    continue

                size[u] += size[v]

                if size[v] > max_size:
                    max_size = size[v]
                    heavy[u] = v

        # 4. HLD: 각 노드의 head, pos 결정
        cur = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1

                for v in g[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # 5. Segment Tree 생성
        base = 1
        while base < n:
            base <<= 1

        tree = [0] * (base * 2)
        chars = list(s)

        def mask(c):
            return 1 << (ord(c) - ord('a'))

        for u in range(n):
            tree[base + pos[u]] = mask(chars[u])

        for i in range(base - 1, 0, -1):
            tree[i] = tree[i * 2] ^ tree[i * 2 + 1]

        # 6. Segment Tree 단일 노드 업데이트
        def update(u, c):
            chars[u] = c
            i = base + pos[u]
            tree[i] = mask(c)

            i //= 2
            while i:
                tree[i] = tree[i * 2] ^ tree[i * 2 + 1]
                i //= 2

        # 7. Segment Tree 구간 XOR
        def seg_query(l, r):
            result = 0
            l += base
            r += base

            while l <= r:
                if l & 1:
                    result ^= tree[l]
                    l += 1

                if not (r & 1):
                    result ^= tree[r]
                    r -= 1

                l //= 2
                r //= 2

            return result

        # 8. HLD 경로 쿼리
        def path_query(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= seg_query(pos[head[u]], pos[u])

                u = parent[head[u]]

            # 같은 체인에 도달
            if depth[u] > depth[v]:
                u, v = v, u

            result ^= seg_query(pos[u], pos[v])

            return result

        # 9. 쿼리 처리
        for q in queries:
            op, a, b = q.split()

            if op == "update":
                update(int(a), b)
            else:
                u, v = int(a), int(b)
                x = path_query(u, v)

                ans.append((x & (x - 1)) == 0)

        return ans
