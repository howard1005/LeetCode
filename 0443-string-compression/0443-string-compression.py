class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        def enc(c,cnt):
            nonlocal i
            chars[i] = c
            i += 1
            if cnt <= 1:
                return
            for nc in list(str(cnt)):
                chars[i] = nc
                i += 1
        
        prev = chars[0]
        cnt = 1
        for c in chars[1:]:
            if c != prev:
                enc(prev,cnt)
                cnt = 1
            else:
                cnt += 1
            prev = c
        enc(prev,cnt)
        
        return i