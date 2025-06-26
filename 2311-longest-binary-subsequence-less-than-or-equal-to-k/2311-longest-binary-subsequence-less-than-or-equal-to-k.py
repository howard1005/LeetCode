class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0

        bl = []
        while k:
            bl.append(k&1)
            k >>= 1
        # print("bl",bl)


        def valid(size):

            if len(bl) > size:
                # print("미달")
                if len(s) >= size:
                    return True
                else:
                    return False

            l = [0 for _ in range(size)]

            for i in range(min(len(l),len(bl))):
                l[i] = bl[i]
            l.reverse()
            print(size,l)

            
            def find(j,c):
                while j<len(s):
                    if s[j] == c:
                        break
                    j += 1
                # print(f"{j}에서 {c}를 찾음")
                return j if j < len(s) else None

            j = 0
            for i,b in enumerate(l):
                if b:
                    # 0을 찾아서 검증
                    jj = find(j,'0')
                    if jj is not None:
                        if len(s)-jj >= len(l)-i:
                            # print("flag1")
                            return True
                    # 1을 찾아서 업데이트
                    jj = find(j,'1')
                    if jj is None:
                        # print("flag2")
                        return False
                    j = jj+1
                else:
                    # 0을 찾아서 업데이트
                    jj = find(j,'0')
                    if jj is None:
                        # print("flag3")
                        return False
                    j = jj+1

            return True


        lo,hi = 1,len(s)
        while lo<=hi:
            mi = (lo+hi)//2
            t = valid(mi)
            # print(f"size {mi} 결과 {t}\n")
            if t:
                lo = mi+1
                ans = max(ans,mi)
            else:
                hi = mi-1
                    
        return ans