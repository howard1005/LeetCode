class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        ans = [0] * len(queries)
        cntd = defaultdict(int)
        i = j = 0

        for q, idx in sorted((q, idx) for idx, q in enumerate(queries)):
            # q 이하의 로그 추가
            while j < len(logs) and logs[j][1] <= q:
                cntd[logs[j][0]] += 1
                j += 1

            # q-x보다 오래된 로그 제거
            while i < j and logs[i][1] < q - x:
                a = logs[i][0]
                cntd[a] -= 1
                if cntd[a] == 0:
                    del cntd[a]
                i += 1

            ans[idx] = n - len(cntd)

        return ans