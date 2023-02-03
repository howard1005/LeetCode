class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        row_idx = 0
        op = 1
        for c in s:
            rows[row_idx].append(c)
            if row_idx == 0 and op == -1:
                op = 1
            elif row_idx == numRows-1 and op == 1:
                op = -1
            row_idx = (row_idx + op) % numRows
        ans = ''
        for row in rows:
            ans += ''.join(row)
        return ans