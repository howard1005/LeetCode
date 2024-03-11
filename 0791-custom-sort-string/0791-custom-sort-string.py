from collections import defaultdict

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        d = defaultdict(int)
        tail = ''
        for c in str:
            if c in order:
                d[c] += 1
            else:
                tail += c
        head = ''
        for c in order:
            head += c*d[c]
        return head + tail