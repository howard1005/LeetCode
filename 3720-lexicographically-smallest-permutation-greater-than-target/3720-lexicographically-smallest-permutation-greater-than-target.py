class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        ans = ''

        count = Counter(s)
        chars = sorted(count)
        n = len(target)

        def remaining():
            return "".join(ch * count[ch] for ch in chars)

        def dfs(i):
            # target과 완전히 같으면 조건 불충족
            if i == n:
                return None

            for ch in chars:
                if count[ch] == 0 or ch < target[i]:
                    continue

                count[ch] -= 1

                if ch > target[i]:
                    # 이미 커졌으므로 나머지는 오름차순으로 붙임
                    return ch + remaining()

                # ch == target[i]
                suffix = dfs(i + 1)
                if suffix is not None:
                    return ch + suffix

                count[ch] += 1  # 백트래킹

            return None

        if len(s) != len(target):
            return ""

        ans = dfs(0)

        return ans if ans else ''