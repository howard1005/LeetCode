class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        cnt = 0
        st = []
        for c in s:
            if c == '(':
                st.append(cnt)
                cnt = 0
            else:
                if st:
                    cnt += 2 + st.pop()
                else:
                    cnt = 0
            ans = max(ans,cnt)
        return ans